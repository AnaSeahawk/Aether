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

active_claimed_paths() {
  grep -v '^#' "$1" | sed 's/ #.*$//' | grep -v '^$' || true
}

assert_contains() {
  local text="$1"
  local expected="$2"
  [[ "$text" == *"$expected"* ]] || fail "expected output to contain: $expected"
}

lane_lock() {
  local role="$1"
  local lane="${2:-$1}"
  if [ "$lane" = "$role" ]; then
    printf '%s/%s.lock\n' "$test_workspace" "$role"
  else
    printf '%s/%s--%s.lock\n' "$test_workspace" "$role" "$lane"
  fi
}

lane_token() {
  local lock
  lock="$(lane_lock "$@")"
  # A lane that lost a race was never written; releasing it is still harmless.
  [ -f "$lock" ] || return 0
  sed -n 's/^# token: //p' "$lock" | head -n 1
}

# Release using the token the claim recorded, the way an owning session does.
release_lane() {
  local role="$1"
  shift
  local lane="$role"
  if [ "${1:-}" = "--lane" ]; then
    lane="$2"
  fi
  "$helper" release "$role" "$@" --token "$(lane_token "$role" "$lane")" >/dev/null
}

"$helper" claim researcher "$test_workspace/legacy" -- legacy >/dev/null
[ -s "$test_workspace/researcher.lock" ] || fail 'legacy claim did not write researcher.lock'
release_lane researcher
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

release_lane researcher --lane caraka-notes
[ ! -s "$test_workspace/researcher--caraka-notes.lock" ] ||
  fail 'dynamic release did not clear its lock'

status_output="$("$helper" status)"
[[ "$status_output" != *'researcher/caraka-notes'* ]] ||
  fail 'released dynamic lane remained in active status'
assert_contains "$status_output" 'researcher/alchemy-notes'

release_lane researcher --lane alchemy-notes

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
  release_lane analyst "${lane_args[@]}"
  release_lane curator
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
release_lane writer
"$helper" claim writer / -- root >/dev/null
expect_status 2 "$helper" claim curator "$test_workspace/free" -- descendant
release_lane writer

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
  release_lane analyst --lane first
  [ "$second_lane" = first ] || release_lane analyst --lane "$second_lane"
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

# A claim records its lane, claim time, epoch, and a release token. Metadata
# lines must never be read back as claimed paths.
claim_output="$("$helper" claim curator "$test_workspace/tokened" -- token work)"
assert_contains "$claim_output" 'Release token for curator: '
curator_lock="$(lane_lock curator)"
assert_contains "$(cat "$curator_lock")" '# lane: curator'
assert_contains "$(cat "$curator_lock")" '# claimed: '
assert_contains "$(cat "$curator_lock")" '# epoch: '
token="$(lane_token curator)"
[[ "$token" =~ ^[0-9a-f]{10}$ ]] || fail "claim did not record a usable token: $token"
assert_contains "$claim_output" "$token"
[ "$(active_claimed_paths "$curator_lock")" = "$test_workspace/tokened" ] ||
  fail 'metadata lines were parsed as claimed paths'

# Another session cannot release this lane: no token, and a wrong token, both
# refuse and leave the claim standing.
expect_status 3 "$helper" release curator
assert_contains "$(cat "$test_workspace/last-output")" 'supply it with --token'
[ -s "$curator_lock" ] || fail 'tokenless release cleared an owned lane'
expect_status 3 "$helper" release curator --token 0000000000
assert_contains "$(cat "$test_workspace/last-output")" 'does not match'
[ -s "$curator_lock" ] || fail 'wrong token cleared an owned lane'

# A fresh lane is not abandoned, so clear refuses it by default.
expect_status 3 "$helper" clear curator
assert_contains "$(cat "$test_workspace/last-output")" 'abandonment threshold'
[ -s "$curator_lock" ] || fail 'clear removed a lane that was not stale'
expect_status 64 "$helper" clear curator --older-than soon
expect_status 64 "$helper" stale --older-than -1

# The owning session releases with its recorded token.
"$helper" release curator --token "$token" >/dev/null
[ ! -s "$curator_lock" ] || fail 'correct token did not release the lane'

# Records written before tokens existed still release, with a warning.
printf '%s\n' "$test_workspace/legacy-record # old" > "$curator_lock"
release_output="$("$helper" release curator --token whatever 2>&1 >/dev/null)"
assert_contains "$release_output" 'predates release tokens'
[ ! -s "$curator_lock" ] || fail 'legacy record was not released'
printf '%s\n' "$test_workspace/legacy-record # old" > "$curator_lock"
"$helper" release curator >/dev/null
[ ! -s "$curator_lock" ] || fail 'legacy record required a token'

# An abandoned lane is findable and reclaimable. Back-date the claim to stand
# in for a session that ended without releasing.
"$helper" claim writer --lane abandoned "$test_workspace/orphaned" -- interrupted >/dev/null
abandoned_lock="$(lane_lock writer abandoned)"
sed -i "s/^# epoch: .*/# epoch: $(( $(date -u +%s) - 172800 ))/" "$abandoned_lock"

stale_output="$("$helper" stale)"
assert_contains "$stale_output" 'writer/abandoned'
assert_contains "$stale_output" "$test_workspace/orphaned"
assert_contains "$stale_output" 'tools/orchestrate clear writer --lane abandoned'
assert_contains "$("$helper" status)" 'STALE'

# The blocked session is told why and what to do about it.
expect_status 2 "$helper" claim curator "$test_workspace/orphaned" -- blocked
assert_contains "$(cat "$test_workspace/last-output")" 'STALE'
assert_contains "$(cat "$test_workspace/last-output")" 'tools/orchestrate stale'

clear_output="$("$helper" clear writer --lane abandoned)"
assert_contains "$clear_output" 'Clearing abandoned lane writer/abandoned'
assert_contains "$clear_output" "$test_workspace/orphaned"
[ ! -s "$abandoned_lock" ] || fail 'clear did not release the abandoned lane'
assert_contains "$("$helper" clear writer --lane abandoned)" 'already idle'

# With the lane cleared, the blocked work proceeds.
"$helper" claim curator "$test_workspace/orphaned" -- unblocked >/dev/null
release_lane curator

# --older-than and --force override the threshold for a lane known to be dead.
"$helper" claim analyst --lane fresh "$test_workspace/fresh" -- fresh >/dev/null
"$helper" clear analyst --lane fresh --older-than 0 >/dev/null
[ ! -s "$(lane_lock analyst fresh)" ] || fail '--older-than 0 did not clear the lane'
"$helper" claim analyst --lane fresh "$test_workspace/fresh" -- fresh >/dev/null
"$helper" clear analyst --lane fresh --force >/dev/null
[ ! -s "$(lane_lock analyst fresh)" ] || fail '--force did not clear the lane'

assert_contains "$("$helper" stale)" 'No lane has been held longer than'

printf '%s\n' 'orchestrate tests passed'
