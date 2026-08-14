# Marketing OS — Execution Layer & MCP Wiring

> **Source of truth moved to `execution/tool-registry.yaml`.** This file is the
> human-readable guide; the registry is what the runtime reads.

The Marketing OS is runtime-agnostic: 137 SKILL.md files that any harness
(Hermes, Claude Code, or Collision's own runtime) can execute. This layer
defines how those skills bind to real tools and the gates that protect the
world-changing ones.

## What is live right now

| Declaration | Real tool | Gate | Status |
|---|---|---|---|
| `mcp:web-search` | parallel_search (web_search + web_fetch) | 🟢 open | **connected** — 52 skills |
| `mcp:web-scraper` | native browser automation | 🟢 open | **connected** — 6 skills |

These two cover **58 of 74 operator skills** — the entire intelligence,
research, audit, and planning surface runs live today with zero credentials.

## What needs credentials (mapped, blocked on you)

| Declaration | Server | Gate | Blocked on |
|---|---|---|---|
| `mcp:ads-platforms` | markifact-mcp (Google+Meta+GA4+TikTok+LinkedIn) | 🔴 | OAuth |
| `mcp:meta-ads` | meta-ads-mcp | 🔴 | OAuth |
| `mcp:analytics` | ga4-mcp | 🟡 | OAuth |
| `mcp:search-console` | google-search-console-mcp | 🟡 | OAuth |
| `mcp:crm` | hubspot-api | 🔴 | OAuth |
| `mcp:email` | gmail-api | 🔴 | OAuth |
| `mcp:email-platform` | klaviyo-api | 🔴 | key |
| `mcp:shopify` | shopify-admin-api | 🔴 | key |
| `mcp:calendar` | google-calendar-api | 🔴 | OAuth |
| `mcp:automation` | n8n-api | 🔴 | key |
| `mcp:heatmap` | hotjar-api | 🟡 | OAuth |
| `mcp:ai-query` | perplexity-api | 🟡 | key |
| `mcp:image-generation` | image-gen-api | 🔴 | key |

## Free installs worth doing next

| Declaration | Server | Gate | Note |
|---|---|---|---|
| `mcp:pagespeed` | pagespeed-api | 🟢 | free, no key at low volume |
| `mcp:reddit-scraper` | reddit .json endpoints | 🟢 | no auth for public listing |
| `mcp:semrush` / `mcp:ahrefs` | open-seo (every-app/open-seo) | 🟢 | free Semrush/Ahrefs alternative |

## Capability gates (enforced by runtime, not skill docs)

| Gate | Meaning |
|---|---|
| 🔴 **gated** | spend, publish, or send-to-human → show exact payload, wait for approval |
| 🟡 **scoped** | read-only by default; any write degrades to 🔴 |
| 🟢 **open** | read/plan/draft — free, no approval |

## Wiring a new tool

1. `hermes config set mcp_servers.<name>.url "<url>"` (or `.command`/`.args` for stdio)
2. Secrets go in `.env`, never in config.yaml
3. Start a new chat session — the running one won't pick up new servers
4. Verify with Hermes's own discovery: `discover_mcp_tools()`
5. Update `tool-registry.yaml` status → `connected`

## How to read the rest

- `execution/tool-registry.yaml` — canonical key → server/gate/status mapping
- `execution/protocol.md` — the strategist→operator execution flow
- `agents/agent-layer.md` — director/specialist/critic roles that enforce gates
