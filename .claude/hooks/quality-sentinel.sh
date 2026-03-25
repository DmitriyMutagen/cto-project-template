#!/bin/bash
# Quality Sentinel Hook (Stop Event)
# Analyzes changed files for risky patterns

CHANGED=$(git diff --name-only 2>/dev/null)
[ -z "$CHANGED" ] && exit 0

WARNINGS=""
PY_FILES=$(echo "$CHANGED" | grep '\.py$')
if [ -n "$PY_FILES" ]; then
    for f in $PY_FILES; do
        [ ! -f "$f" ] && continue
        grep -qP 'except.*:\s*$' "$f" 2>/dev/null && WARNINGS="$WARNINGS\n  [RISK] $f: bare except — add logging/Sentry?"
        grep -qP '(execute|raw)\s*\(\s*f"|\.format\(' "$f" 2>/dev/null && WARNINGS="$WARNINGS\n  [RISK] $f: possible raw SQL — parameterize?"
        grep -qP 'os\.environ\[' "$f" 2>/dev/null && WARNINGS="$WARNINGS\n  [INFO] $f: direct os.environ — use config/settings?"
    done
fi

[ -n "$WARNINGS" ] && echo -e "Quality Sentinel:\n$WARNINGS"
exit 0
