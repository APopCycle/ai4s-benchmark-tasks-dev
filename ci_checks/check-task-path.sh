#!/usr/bin/env bash
# Validate the taxonomy-aware task layout.
#
# Non-engineering: tasks/<primary-domain>/<task>/
# Engineering:     tasks/engineering-sciences/<secondary-discipline>/<task>/
# Flat lite/ and archive/ tasks carry the same classification in task.toml.

set -e

TASK_DIR="${1:-}"
if [ -z "$TASK_DIR" ]; then
    echo "Usage: check-task-path.sh <task-dir>"
    exit 2
fi
TASK_DIR="${TASK_DIR%/}"

POOL_FILE=""
for candidate in \
    "$GITHUB_WORKSPACE/base/.github/reviewer-pool.yml" \
    ".github/reviewer-pool.yml"; do
    if [ -f "$candidate" ]; then
        POOL_FILE="$candidate"
        break
    fi
done
if [ -z "$POOL_FILE" ]; then
    echo "FAIL $TASK_DIR: couldn't locate .github/reviewer-pool.yml"
    exit 1
fi

python3 - "$TASK_DIR" "$POOL_FILE" <<'PYEOF'
import os
import re
import sys

task_dir, pool_file = sys.argv[1], sys.argv[2]

DOMAINS = {
    "mathematical-sciences",
    "physical-sciences",
    "chemical-materials-sciences",
    "life-sciences",
    "medical-neuroscience-health-sciences",
    "earth-environmental-sciences",
    "computer-information-sciences",
    "engineering-sciences",
}


def registry_keys(section):
    try:
        import yaml
        with open(pool_file, encoding="utf-8") as handle:
            data = yaml.safe_load(handle) or {}
        return set((data.get(section) or {}).keys())
    except (ImportError, OSError):
        with open(pool_file, encoding="utf-8") as handle:
            text = handle.read()
        match = re.search(rf"^{re.escape(section)}:\s*\n(.+?)(?:\n\S|\Z)", text, re.MULTILINE | re.DOTALL)
        return {
            item.group(1)
            for line in (match.group(1).splitlines() if match else [])
            if (item := re.match(r"\s+([a-z-]+)\s*:", line))
        }


ENGINEERING_DISCIPLINES = registry_keys("domain_chairs_by_engineering_discipline")
if not ENGINEERING_DISCIPLINES:
    print(f"FAIL {task_dir}: engineering discipline registry is empty or unreadable")
    sys.exit(1)

parts = task_dir.split("/")
flat = bool(parts) and parts[0] in ("lite", "archive")
if flat:
    if len(parts) != 2:
        print(f"FAIL {task_dir}: expected {parts[0]}/<task>/")
        sys.exit(1)
    expected_domain = None
    expected_discipline = None
else:
    if not parts or parts[0] != "tasks":
        print(f"FAIL {task_dir}: not under tasks/, lite/ or archive/")
        sys.exit(1)
    if len(parts) == 3:
        expected_domain, _ = parts[1:]
        expected_discipline = ""
        if expected_domain == "engineering-sciences":
            print(f"FAIL {task_dir}: Engineering Sciences tasks require tasks/engineering-sciences/<secondary-discipline>/<task>/")
            sys.exit(1)
    elif len(parts) == 4 and parts[1] == "engineering-sciences":
        _, expected_domain, expected_discipline, _ = parts
        if expected_discipline not in ENGINEERING_DISCIPLINES:
            print(f"FAIL {task_dir}: invalid Engineering Sciences secondary discipline '{expected_discipline}'")
            print(f"     Valid: {', '.join(sorted(ENGINEERING_DISCIPLINES))}")
            sys.exit(1)
    else:
        print(f"FAIL {task_dir}: expected tasks/<domain>/<task>/, or tasks/engineering-sciences/<secondary-discipline>/<task>/")
        sys.exit(1)

    if expected_domain not in DOMAINS:
        print(f"FAIL {task_dir}: invalid primary-domain directory '{expected_domain}'")
        print(f"     Valid: {', '.join(sorted(DOMAINS))}")
        sys.exit(1)

toml_path = os.path.join(task_dir, "task.toml")
if not os.path.isfile(toml_path):
    sys.exit(0)
try:
    import tomllib
    with open(toml_path, "rb") as handle:
        metadata = (tomllib.load(handle).get("metadata") or {})
except Exception as exc:
    print(f"FAIL {task_dir}: cannot read task.toml classification: {exc}")
    sys.exit(1)

domain = str(metadata.get("domain") or "").strip()
discipline = str(metadata.get("field") or "").strip()
if domain not in DOMAINS:
    print(f"FAIL {task_dir}: invalid [metadata].domain '{domain}'")
    print(f"     Valid: {', '.join(sorted(DOMAINS))}")
    sys.exit(1)
if domain == "engineering-sciences":
    if discipline not in ENGINEERING_DISCIPLINES:
        print(f"FAIL {task_dir}: Engineering Sciences tasks require [metadata].field to be a valid secondary discipline")
        print(f"     Valid: {', '.join(sorted(ENGINEERING_DISCIPLINES))}")
        sys.exit(1)
elif discipline:
    print(f"FAIL {task_dir}: [metadata].field must be empty outside Engineering Sciences; use required subfield for the free-text research area")
    sys.exit(1)

if not flat:
    if domain != expected_domain:
        print(f"FAIL {task_dir}: [metadata].domain = '{domain}' but folder is under '{expected_domain}'")
        sys.exit(1)
    if discipline != expected_discipline:
        print(f"FAIL {task_dir}: [metadata].field = '{discipline}' but folder uses '{expected_discipline}'")
        sys.exit(1)

sys.exit(0)
PYEOF
