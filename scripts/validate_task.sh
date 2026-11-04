#!/usr/bin/env bash
# Run Harbor oracle and nop, requiring exact binary mean rewards 1 and 0.
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <task-dir>" >&2
  exit 2
fi
TASK_DIR="${1%/}"
OUT_ROOT=$(mktemp -d "${TMPDIR:-/tmp}/ai4s-harbor-validation.XXXXXX")

run_and_reward() {
  local agent="$1" out="$2" log="$3"
  # Keep Harbor's build/run stream visible even though this function is used
  # in command substitution. Only the parsed reward is emitted on stdout.
  harbor run -p "$TASK_DIR" --agent "$agent" -o "$out" 2>&1 | tee "$log" >&2
  sed -nE 's/.*Mean[:[:space:]]+([0-9]+([.][0-9]+)?).*/\1/p' "$log" | tail -1
}

oracle_reward=$(run_and_reward oracle "$OUT_ROOT/oracle" "$OUT_ROOT/oracle.log")
if [ "$oracle_reward" != "1" ] && [ "$oracle_reward" != "1.0" ] && [ "$oracle_reward" != "1.000" ]; then
  echo "FAIL: oracle mean reward is ${oracle_reward:-unparseable}, expected 1" >&2
  echo "Logs retained at $OUT_ROOT" >&2
  exit 1
fi

nop_reward=$(run_and_reward nop "$OUT_ROOT/nop" "$OUT_ROOT/nop.log")
if [ "$nop_reward" != "0" ] && [ "$nop_reward" != "0.0" ] && [ "$nop_reward" != "0.000" ]; then
  echo "FAIL: nop mean reward is ${nop_reward:-unparseable}, expected 0" >&2
  echo "Logs retained at $OUT_ROOT" >&2
  exit 1
fi

echo "PASS: oracle=$oracle_reward nop=$nop_reward"
echo "Run artifacts: $OUT_ROOT"
