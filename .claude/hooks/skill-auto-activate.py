#!/usr/bin/env python3
"""Skills Auto-Activation Hook (UserPromptSubmit) — CRITICAL.
Without this, skills are ignored in ~90% of cases."""
import os, re, json, sys

prompt = os.environ.get("CLAUDE_USER_PROMPT", "")
if not prompt:
    try:
        prompt = json.loads(sys.stdin.read()).get("prompt", "")
    except Exception:
        prompt = ""

prompt_lower = prompt.lower()
SKILL_MAP = {
    r"plan|design|architect|структур|проектиров": ["Use /superpowers:brainstorming + /superpowers:writing-plans"],
    r"test|tdd|тест|coverage": ["Use /superpowers:test-driven-development (Red-Green-Refactor)"],
    r"bug|fix|ошибк|баг|error|debug": ["Use /superpowers:systematic-debugging", "Check sentry-mcp: list_issues FIRST"],
    r"review|ревью|pr": ["Use /superpowers:requesting-code-review"],
    r"spec|требован|requirement|фича|feature": ["Use /kiro:spec-init for SDD"],
    r"branch|ветк": ["Use /superpowers:using-git-worktrees"],
    r"deploy|деплой|release": ["Use /superpowers:verification-before-completion"],
    r"refactor|рефактор": ["Use /superpowers:subagent-driven-development", "Use Serena find_referencing_symbols FIRST"],
    r"библиотек|library|docs|api|документац": ["Use Context7 MCP for up-to-date docs"],
    r"навигац|symbol|функци|class": ["Use Serena MCP for semantic navigation"],
}

activations = []
for pattern, skills in SKILL_MAP.items():
    if re.search(pattern, prompt_lower):
        activations.extend(skills)

if activations:
    seen = set()
    unique = [a for a in activations if a not in seen and not seen.add(a)]
    print("SKILL ACTIVATION:\n" + "\n".join(f"  -> {s}" for s in unique[:5]))
