#!/usr/bin/env bash
# Positive and negative regression tests for the file-proposal validator.
set -euo pipefail

ROOT=$(cd "$(dirname "$0")/.." && pwd)
TMP=$(mktemp -d "${TMPDIR:-/tmp}/ai4s-validator-tests.XXXXXX")
trap 'rm -rf "$TMP"' EXIT
mkdir -p "$TMP/proposals/earth-environmental-sciences"
VALID="$ROOT/proposals/examples/sparse-network-assimilation.md"

expect_fail() {
  local name="$1" file="$2"
  if python3 "$ROOT/scripts/check_proposal.py" --repo-root "$TMP" "$file" >/dev/null 2>&1; then
    echo "FAIL: negative fixture unexpectedly passed: $name" >&2
    exit 1
  fi
  echo "PASS negative: $name"
}

python3 "$ROOT/scripts/check_proposal.py" "$VALID" >/dev/null
echo "PASS positive: official normalized example"

cp "$VALID" "$TMP/proposals/earth-environmental-sciences/invalid-type.md"
sed -i 's/`workflow_automation`/`both`/' "$TMP/proposals/earth-environmental-sciences/invalid-type.md"
expect_fail invalid-type "$TMP/proposals/earth-environmental-sciences/invalid-type.md"

cp "$VALID" "$TMP/proposals/earth-environmental-sciences/missing-contact.md"
sed -i '/联系方式 \/ Contact:/d' "$TMP/proposals/earth-environmental-sciences/missing-contact.md"
expect_fail missing-contact "$TMP/proposals/earth-environmental-sciences/missing-contact.md"

cp "$VALID" "$TMP/proposals/earth-environmental-sciences/invalid-domain.md"
sed -i 's/`earth-environmental-sciences`/`not-a-domain`/' "$TMP/proposals/earth-environmental-sciences/invalid-domain.md"
expect_fail invalid-domain "$TMP/proposals/earth-environmental-sciences/invalid-domain.md"

cp "$VALID" "$TMP/proposals/earth-environmental-sciences/empty-section.md"
perl -0pi -e 's/(## 10\.[^\n]*\n).*?(?=\n## 11\.)/$1/s' "$TMP/proposals/earth-environmental-sciences/empty-section.md"
expect_fail empty-section "$TMP/proposals/earth-environmental-sciences/empty-section.md"

cp "$ROOT/proposals/examples/onsager-ising-lean.md" "$TMP/proposals/earth-environmental-sciences/frontier-no-sota.md"
sed -i 's/^- 当前 SOTA \/ Current SOTA:.*/- 当前 SOTA \/ Current SOTA: None/' "$TMP/proposals/earth-environmental-sciences/frontier-no-sota.md"
expect_fail frontier-no-sota "$TMP/proposals/earth-environmental-sciences/frontier-no-sota.md"

cp "$VALID" "$TMP/proposals/earth-environmental-sciences/duplicate-a.md"
cp "$VALID" "$TMP/proposals/earth-environmental-sciences/duplicate-b.md"
expect_fail duplicate-proposal-id "$TMP/proposals/earth-environmental-sciences/duplicate-a.md"

echo "All proposal validator regression tests passed."
