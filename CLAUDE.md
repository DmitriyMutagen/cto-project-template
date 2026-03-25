# PROJECT_NAME — Claude Code Configuration

## Project Overview
**One-line description**: TODO
**Tech Stack**: TODO (e.g., FastAPI + SQLAlchemy 2.0 + PostgreSQL + Redis)
**Domain**: TODO

## Architecture (Clean Architecture — strict dependency rule)
```
Presentation → Application → Domain ← Infrastructure
(src/api/)     (src/services/) (src/domain/) (src/infrastructure/)
```
Domain has ZERO external dependencies. Infrastructure adapts external services.

## Behavioral Patterns (CTO-Level)
See `.claude/architecture/behavioral-patterns.md` for full details:
- **Confidence Check**: >90% execute, 70-89% show alternatives, <70% ask human
- **Self-Check**: verify vs requirements after each block
- **Reflexion**: log failures to `.claude/memory/permanent/reflexion.md`
- **Wave-Checkpoint-Wave**: parallel reads → consolidate → parallel writes

## Workflow: Explore → Plan → Code → Commit
1. **Explore** — read files, DO NOT CODE. Use Serena + Context7
2. **Plan** — Planning Mode, think/ultrathink, 2-3 alternatives with pros/cons
3. **Code** — fresh session with plan, 1-2 sections, TDD (Red-Green-Refactor)
4. **Commit** — Conventional Commits, PR, quality gates

## SDD (Spec-Driven Development)
For features >1 day: /kiro:spec-init → spec → design → tasks → implement → review
Quality Gates between each phase. Specs in `docs/todo/`, completed in `docs/done/`

## Mandatory Tools
- **Serena**: activate_project, find_symbol, find_referencing_symbols BEFORE refactoring
- **Sentry**: list_issues BEFORE fixing bugs, check after deploy
- **Context7**: ALWAYS check library docs, never guess APIs

## Skill Workflow (complex features)
1. `/brainstorm` → questions, edge cases, trade-offs
2. `/writing-plans` → chunks of 2-5 min, sign-off each
3. `/test-driven-development` → tests FIRST
4. `/verification-before-completion` → self-validate before done

## Heavy Words (use instead of long descriptions)
YAGNI, KISS, SOLID, Clean Architecture dependency rule, DRY,
Idempotent UPSERT, Tenacity retry + exponential backoff

## Development Rules
1. Strict type hints, async/await, modern patterns
2. All external API calls: tenacity retry (3 attempts, exponential backoff)
3. Timeouts: API 30s, AI 60s, DB 10s
4. Avoid N+1 — use selectinload/joinedload
5. UPSERT for idempotent sync operations

## Anti-patterns (NEVER do)
- Vibe coding without spec → use SDD
- @-file imports in CLAUDE.md → use references
- Let context hit limit → clear at 30-50%
- Skip observability → Sentry from day 1

## Quality Gates
- Pre-commit: ruff + ast-grep + secret detection
- CI: pytest + lint + security scan
- Deploy: Sentry release tracking

## Running
```bash
# Backend
pip install -r requirements.txt
uvicorn src.api.main:app --reload --port 8000
# Tests
pytest tests/ -v
```

## Memory
- Permanent: `.claude/memory/permanent/` (decisions, gotchas, reflexion)
- Sprint: `.claude/memory/decay-7d/progress.md`
- Research: `.claude/memory/decay-30d/`
