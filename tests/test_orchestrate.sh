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

expect_status() {
  local expected="$1"
  shift
  local actual=0
  "$@" >"$test_workspace/last-output" 2>&1 || actual=$?
  [ "$actual" -eq "$expected" ] || fail "expected exit $expected, received $actual"
}

# A second session cannot replace an active default or dynamic lane. A failed
# request must preserve the previous record, including its reason.
for lane in analyst analyst--retained; do
  lane_args=()
  [ "$lane" = analyst ] || lane_args=(--lane retained)
  "$helper" claim analyst "${lane_args[@]}" "$test_workspace/owned" -- original >/dev/null
  original="$(cat "$test_workspace/$lane.lock")"
  "$helper" claim curator "$test_workspace/peer" -- peer >/dev/null
  expect_status 2 "$helper" claim analyst "${lane_args[@]}" "$test_workspace/peer" -- replacement
  [ "$(cat "$test_workspace/$lane.lock")" = "$original" ] || fail 'conflict erased the original claim'
  expect_status 2 "$helper" claim analyst "${lane_args[@]}" "$test_workspace/unrelated" -- replacement
  [ "$(cat "$test_workspace/$lane.lock")" = "$original" ] || fail 'active lane was silently replaced'
  "$helper" release analyst "${lane_args[@]}" >/dev/null
  "$helper" release curator >/dev/null
done

# Normalized aliases and ancestor claims must respect an existing file claim.
mkdir -p "$test_workspace/tree/child"
ln -s "$test_workspace/tree" "$test_workspace/alias"
"$helper" claim writer "$test_workspace/tree/child/file.md" -- file >/dev/null
for path in "$test_workspace/tree" "$test_workspace/alias/child/file.md" /; do
  expect_status 2 "$helper" claim curator "$path" -- ancestor
done
expect_status 2 "$helper" claim curator "$test_workspace/free" "$test_workspace/tree" -- atomic
[ ! -s "$test_workspace/curator.lock" ] || fail 'rejected multipath request left a partial claim'
"$helper" release writer >/dev/null
"$helper" claim writer / -- root >/dev/null
expect_status 2 "$helper" claim curator "$test_workspace/free" -- descendant
"$helper" release writer >/dev/null

for invalid_path in relative "$test_workspace/bad # record" "$test_workspace/trailing " $'/bad\nrecord'; do
  expect_status 64 "$helper" claim curator "$invalid_path" -- invalid
done
expect_status 64 "$helper" claim curator "$test_workspace/free" -- $'bad\nreason'

# Queue two processes behind the transaction guard. Exactly one overlapping
# claim succeeds; distinct claims can both succeed. Active lane reuse also
# rejects one claimant even when the requested paths do not overlap.
parallel_claims() {
  local second_lane="$1" second_path="$2" expected="$3"
  local first_pid second_pid
  rm -f "$test_workspace/first-ready" "$test_workspace/second-ready" \
    "$test_workspace/first-status" "$test_workspace/second-status"
  exec 8>"$test_workspace/.orchestrate.guard.lock"
  flock -x 8
  (
    exec 8>&-
    touch "$test_workspace/first-ready"
    result=0
    "$helper" claim analyst --lane first "$test_workspace/parallel/a" -- first \
      >"$test_workspace/first-output" 2>&1 || result=$?
    printf '%s\n' "$result" >"$test_workspace/first-status"
  ) &
  first_pid=$!
  (
    exec 8>&-
    touch "$test_workspace/second-ready"
    result=0
    "$helper" claim analyst --lane "$second_lane" "$second_path" -- second \
      >"$test_workspace/second-output" 2>&1 || result=$?
    printf '%s\n' "$result" >"$test_workspace/second-status"
  ) &
  second_pid=$!
  for _ in {1..100}; do
    [ -e "$test_workspace/first-ready" ] && [ -e "$test_workspace/second-ready" ] && break
    sleep 0.01
  done
  [ -e "$test_workspace/first-ready" ] && [ -e "$test_workspace/second-ready" ] || fail 'claim processes did not start'
  sleep 0.1
  [ ! -e "$test_workspace/first-status" ] && [ ! -e "$test_workspace/second-status" ] || fail 'claim bypassed transaction guard'
  flock -u 8
  exec 8>&-
  wait "$first_pid" "$second_pid"
  statuses="$(sort "$test_workspace/first-status" "$test_workspace/second-status" | tr '\n' ' ')"
  [ "$statuses" = "$expected" ] || fail "parallel claim results: $statuses"
  "$helper" release analyst --lane first >/dev/null
  [ "$second_lane" = first ] || "$helper" release analyst --lane "$second_lane" >/dev/null
}

parallel_claims second "$test_workspace/parallel/a/child" '0 2 '
parallel_claims second "$test_workspace/parallel/b" '0 0 '
parallel_claims first "$test_workspace/parallel/b" '0 2 '

# A missing transaction-lock dependency must stop before any claim is written.
mkdir "$test_workspace/no-flock"
for dependency in bash dirname realpath; do
  ln -s "$(command -v "$dependency")" "$test_workspace/no-flock/$dependency"
done
expect_status 69 env PATH="$test_workspace/no-flock" "$helper" claim curator "$test_workspace/free" -- missing-flock
[ ! -s "$test_workspace/curator.lock" ] || fail 'missing flock allowed a claim'

printf '%s\n' 'orchestrate tests passed'
