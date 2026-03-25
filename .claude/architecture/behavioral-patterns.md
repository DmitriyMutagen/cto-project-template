# CTO-Level Behavioral Patterns

## 1. Confidence Check (before ANY task)
Rate confidence 0-100% before executing:
- **>90%** — proceed with implementation
- **70-89%** — present 2-3 alternative approaches with pros/cons, let human decide
- **<70%** — STOP. Ask human for clarification. Do NOT guess.
- ROI: 200 tokens on check saves 50,000 on wrong direction

## 2. Self-Check (after each architectural block)
After generating code:
- Verify output against original requirements
- Run lint + type check mentally
- Check for security violations (OWASP top 10)
- Ensure no architectural boundary violations

## 3. Reflexion (cross-session learning)
When something fails or produces suboptimal results:
- Log to `.claude/memory/permanent/reflexion.md`
- Include: what failed, why, what to do instead
- Next session reads this — avoids repeating known failures
- Auto-update on repeated errors

## 4. Cognitive Personas (focus flags)
Switch attention weights based on task:
| Flag | Focus |
|------|-------|
| --architect | System abstractions, scaling, contracts, microservices |
| --security | OWASP, injections, leaks, authorization, encryption |
| --performance | Profiling, cache, N+1, indexes, query optimization |
| --frontend | UI/UX, components, accessibility, responsive design |
| --backend | APIs, DB schemas, queues, services, migrations |
| --data | Analytics, pipelines, ETL, data quality |
| --qa | Tests, coverage, edge cases, regression |
| --devops | Docker, CI/CD, monitoring, infrastructure, deploys |
| --ml | Models, training, inference, evaluation |

## 5. Wave-Checkpoint-Wave (3.5x speedup)
For large tasks:
- **Wave 1**: Read 10+ files in parallel, gather all context
- **Checkpoint**: Consolidate information, make decisions
- **Wave 2**: Generate changes to independent modules in parallel
- Never modify coupled modules in same wave

## 6. Heavy Words (token-efficient instructions)
Use dense engineering terms instead of verbose descriptions:
- "YAGNI" = don't add features speculatively
- "KISS" = simplest solution that works
- "SOLID boundaries" = respect interface segregation
- "Clean Architecture dependency rule" = dependencies point inward only
- "Idempotent UPSERT" = safe to retry without side effects
- "Tenacity retry + exponential backoff" = resilient external calls
- "DRY" = extract common patterns, don't copy-paste

## 7. Anti-patterns (NEVER do)
| Anti-pattern | Why dangerous | Solution |
|---|---|---|
| Vibe coding without spec | Tech debt exponential | SDD workflow |
| >20k tokens on MCP tools | Destroys useful context | Max 3-5 powerful gateways |
| Auto-formatting in hooks | 160k tokens per 3 rounds | Format in CI/CD |
| RAG for code search | Hidden failures | Serena/ripgrep |
| Complex multi-agent swarms | Debug exponentially harder | Clone Pattern |
| Let context hit limit | Quality degrades | Clear at 30-50% |
| @-file imports in CLAUDE.md | Embeds full text every prompt | Use references |
| No observability | Blind to errors | Sentry + OTel from day 1 |
