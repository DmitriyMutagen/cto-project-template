# CTO-Level Project Template for Claude Code

Production-grade starter template implementing the 10-layer CTO architecture for AI-assisted development with Claude Code.

## Philosophy

This template transforms Claude Code from a reactive assistant into a **deterministic software factory** with quality gates, behavioral patterns, and structured workflows.

Without quality gates, a 5-phase pipeline with 80% accuracy per phase yields only **0.8^5 = 33%** quality. Each gate between phases is a mandatory safety layer.

## What's Included

### Architecture (.claude/)
- **5 Agent Profiles**: solution-architect, fullstack-developer, qa-engineer, security-auditor, devops-engineer
- **Behavioral Patterns**: Confidence Check, Self-Check, Reflexion, 9 Cognitive Personas, Wave-Checkpoint-Wave
- **Dependency Rules**: Clean Architecture with strict inward-only dependency rule
- **MCP Strategy**: Max 3-5 powerful gateways (not API mirrors)

### Memory System (.claude/memory/)
- **Permanent**: decisions.md, gotchas.md, reflexion.md (never deleted)
- **Decay 7d**: sprint progress (loses relevance after a week)
- **Decay 30d**: research results (loses relevance after a month)

### Quality Gates
- **Pre-commit**: ruff linting + secret detection (.pre-commit-config.yaml)
- **CI/CD**: pytest + lint + security scan (.github/workflows/)
- **Hooks**: Quality Sentinel (Stop), Skills Auto-Activation (UserPromptSubmit)

### Documentation (docs/)
- **todo/**: Active specifications (agent focuses here)
- **done/**: Completed specifications (archive)
- **specs/**: Specification template (EARS format)
- **adr/**: Architecture Decision Records
- **artifacts/**: Plans, logs, evidence

### Project Structure (Clean Architecture)
```
src/
  api/            # Presentation layer (HTTP, routers)
  services/       # Application layer (use cases)
  domain/         # Domain layer (entities, zero deps)
  infrastructure/ # Infrastructure (DB, external APIs)
tests/
```

## Workflows

### For New Features (SDD - Spec-Driven Development)
1. `/brainstorm` - Socratic questions, edge cases
2. `/writing-plans` - Structured plan in 2-5 min chunks
3. Create spec in `docs/todo/feature-name.md`
4. `/test-driven-development` - Tests FIRST
5. `/verification-before-completion` - Self-validate
6. Move spec to `docs/done/`

### Official Anthropic Workflow
1. **Explore** - Read files, DO NOT CODE (Serena + Context7)
2. **Plan** - Planning Mode, think/ultrathink, 2-3 alternatives
3. **Code** - Fresh session with plan, 1-2 sections at a time
4. **Commit** - Conventional Commits, PR, quality gates

## Quick Start

```bash
# Copy template
cp -r ~/Documents/project-template/ ~/Documents/my-new-project/
cd ~/Documents/my-new-project/

# Edit mission and config
nano mission.md          # Set project objective
nano CLAUDE.md           # Update tech stack
nano .serena/project.yml # Set project name
nano .env.example        # Set env vars template

# Initialize
git init && git add -A && git commit -m "init: CTO-level project from template"
pip install pre-commit && pre-commit install
```

## Required Global Tools

These must be installed globally (one-time setup):

| Tool | Install | Purpose |
|------|---------|---------|
| SuperClaude v4.3.0 | `pipx install superclaude && superclaude install` | 31 /sc: commands + 15 agents |
| obra/superpowers | Plugin marketplace | TDD, brainstorming, verification skills |
| cc-sdd | `gh repo clone gotalab/cc-sdd ~/.claude/plugins/cc-sdd` | Spec-Driven Development |
| parry-guard | `gh repo clone vaporif/parry-guard ~/.claude/plugins/parry-guard` | Prompt injection scanner |
| Dippy | `gh repo clone ldayton/Dippy ~/.claude/plugins/dippy` | Permission fatigue resolver |

## Based On

- Document: "Architecture and Ecosystem of AI Development with Claude Code: CTO-Level Practices (2026)"
- 10-layer architecture: Project Structure, SuperClaude, TDD/Superpowers, SDD, Memory, Hooks, Subagents, Observability, MCP, Documentation

## License

MIT
