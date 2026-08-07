#!/usr/bin/env bash
set -euo pipefail

repository_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
helper="$repository_root/tools/orchestrate"
test_workspace="$(mktemp -d)"
trap 'rm -rf -- "$test_workspace"' EXIT

export ORCHESTRATE_WORKSPACE_ROOT="$test_workspace"
mkdir -p \
  "$test_workspace/legacy" \
  "$test_workspace/research/caraka" \
  "$test_workspace/research/alchemy"

fail() {
  printf 'FAIL: %s\n' "$1" >&2
  exit 1
}

assert_contains() {
  local text="$1"
  local expected="$2"
  [[ "$text" == *"$expected"* ]] || fail "expected output to contain: $expected"
}

"$helper" claim researcher "$test_workspace/legacy" -- legacy >/dev/null
[ -s "$test_workspace/researcher.lock" ] || fail 'legacy claim did not write researcher.lock'
"$helper" release researcher >/dev/null
[ ! -s "$test_workspace/researcher.lock" ] || fail 'legacy release did not clear researcher.lock'

"$helper" claim researcher --lane caraka-notes \
  "$test_workspace/research/caraka" -- source notes >/dev/null
"$helper" claim researcher --lane alchemy-notes \
  "$test_workspace/research/alchemy" -- source notes >/dev/null

[ -s "$test_workspace/researcher--caraka-notes.lock" ] ||
  fail 'first dynamic lane did not write its lock'
[ -s "$test_workspace/researcher--alchemy-notes.lock" ] ||
  fail 'second dynamic lane did not write its lock'

status_output="$("$helper" status)"
assert_contains "$status_output" 'researcher/caraka-notes'
assert_contains "$status_output" 'researcher/alchemy-notes'

set +e
conflict_output="$("$helper" claim researcher --lane duplicate-notes \
  "$test_workspace/research/caraka/chapter-one" -- overlapping work 2>&1)"
conflict_status=$?
set -e

[ "$conflict_status" -eq 2 ] || fail 'overlapping dynamic claim did not exit 2'
assert_contains "$conflict_output" 'held by researcher/caraka-notes'
[ ! -s "$test_workspace/researcher--duplicate-notes.lock" ] ||
  fail 'rejected dynamic claim was not cleared'

set +e
cross_role_output="$("$helper" claim writer --lane caraka-draft \
  "$test_workspace/research/caraka/draft" -- overlapping role 2>&1)"
cross_role_status=$?
set -e

[ "$cross_role_status" -eq 2 ] || fail 'cross-role overlap did not exit 2'
assert_contains "$cross_role_output" 'held by researcher/caraka-notes'

set +e
"$helper" claim researcher --lane Bad_Lane \
  "$test_workspace/research/caraka" -- invalid >/dev/null 2>&1
invalid_status=$?
set -e

[ "$invalid_status" -eq 64 ] || fail 'invalid lane did not exit 64'

"$helper" release researcher --lane caraka-notes >/dev/null
[ ! -s "$test_workspace/researcher--caraka-notes.lock" ] ||
  fail 'dynamic release did not clear its lock'

status_output="$("$helper" status)"
[[ "$status_output" != *'researcher/caraka-notes'* ]] ||
  fail 'released dynamic lane remained in active status'
assert_contains "$status_output" 'researcher/alchemy-notes'

"$helper" release researcher --lane alchemy-notes >/dev/null

printf '%s\n' 'orchestrate tests passed'
