# MCP Strategy — Minimal & Powerful

## Rule: MAX 3-5 powerful gateways (not API mirrors)

## Scripting Model (preferred)
BAD: 50 individual CRUD tools (read_user, update_order)
GOOD: powerful gateways (execute_code, download_data, take_action)
MCP handles auth + security, Claude scripts against data.

## Recommended Stack
1. **Context7** — up-to-date library documentation (prevents hallucinated APIs)
2. **Serena** — semantic code navigation (LSP-level, better than grep)
3. **Playwright** — browser automation, E2E testing
4. **Sentry** — production error monitoring + AI analysis
5. **vexp** — AST-based context memory (65-70% token savings)

## Project-specific (add as needed)
- Database MCP — for direct SQL access
- Domain API MCP — unified gateway for business domain
