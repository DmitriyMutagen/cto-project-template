# Agent Guide

## Must-Read Files (Before Any Work)
- `mission.md` — project objective and constraints
- `CLAUDE.md` — development rules and architecture
- `.claude/architecture/behavioral-patterns.md` — CTO-level patterns
- `docs/todo/` — active specifications (current focus)

## Artifact-First Workflow
- For non-trivial tasks: create plan in `docs/artifacts/plans/`
- Store test/log output in `docs/artifacts/logs/`
- Keep artifacts lightweight and deterministic

## Build / Test Commands
- Setup: `pip install -r requirements.txt`
- Run: `uvicorn src.api.main:app --reload`
- Tests: `pytest tests/ -v`
- Lint: `ruff check . --fix`

## Architecture
Clean Architecture with strict dependency rule:
- `src/api/` — Presentation (HTTP handlers, routers)
- `src/services/` — Application (use cases, business logic)
- `src/domain/` — Domain (entities, interfaces, zero dependencies)
- `src/infrastructure/` — Infrastructure (DB, external APIs, adapters)

## Subagent Profiles
See `.claude/agents/` for specialized profiles:
- solution-architect — ADR + plans ONLY, no code
- fullstack-developer — implement by spec
- qa-engineer — tests + coverage
- security-auditor — OWASP audit
- devops-engineer — Docker, CI/CD
