# Marketing OS — Execution Layer & MCP Wiring Map

This maps the Marketing OS skills to concrete execution tools (MCP servers, APIs, CLIs) so the system can *act*, not just advise. Every integration is classified by capability gate.

## Capability gates

| Gate | Meaning | Applies to |
|---|---|---|
| 🔴 GATED (approval) | Requires explicit human approval before the action runs | Spend/budget changes, publishing, sending to humans, CRM mutations, campaign launches |
| 🟡 SCOPED (read-mostly) | Read freely; writes allowed only within a declared scope | Reporting pulls, analytics queries, draft creation |
| 🟢 OPEN (read-only) | No approval needed | Search, research, audits, analysis |

**Rule: no integration defaults to write access.** A skill's `allowed_tools` field declares intent; the runtime must enforce the gate, not the skill doc.

---

## MCP servers (from research/oss-landscape.md)

### Paid media

| Server | Repo (stars) | Covers | Gate | Skills served |
|---|---|---|---|---|
| google-ads-mcp | googleads/google-ads-mcp (854) | Google Ads — official | 🔴 writes, 🟡 reads | google-ads |
| meta-ads-mcp | pipeboard-co/meta-ads-mcp (1.2k) | Meta Ads | 🔴 writes, 🟡 reads | meta-ads |
| markifact-mcp | markifact/markifact-mcp (45) | Google, Meta, GA4, TikTok, LinkedIn (300+ ops) | 🔴/🟡 | google-ads, meta-ads, linkedin-ads, tiktok-ads, analytics-setup |
| ads-mcp | amekala/ads-mcp (82) | Google, Meta, LinkedIn, TikTok (100+ tools) | 🔴/🟡 | cross-platform |
| tiktok-ads-mcp-server | AdsMCP/tiktok-ads-mcp-server (48) | TikTok Ads Marketing API | 🔴/🟡 | tiktok-ads |
| linkedin-ads-mcp | danielpopamd/linkedin-ads-mcp (29) | LinkedIn Ads data | 🟡 | linkedin-ads |
| meta-ads-analyzer | mathiaschu/meta-ads-analyzer (410) | Breakdown Effect, Learning Phase diagnosis | 🟡 | meta-ads |

**Notes:**
- The single highest-leverage install is `markifact-mcp` — one server, five platforms, read-mostly by default.
- Official `googleads/google-ads-mcp` is the safest for Google (maintained by Google).
- All paid MCPs need OAuth credentials from the advertiser's ad accounts. Nothing can be wired without those.

### Analytics

| Server | Repo (stars) | Covers | Gate | Skills served |
|---|---|---|---|---|
| google-meta-ads-ga4-mcp | irinabuht12-oss/google-meta-ads-ga4-mcp (1k) | Google Ads, Meta, GA4 (250+ tools) | 🟡 | analytics-setup, funnel-analysis |

### SEO / GEO

| Tool | Type | Covers | Gate | Skills served |
|---|---|---|---|---|
| every-app/open-seo (11.8k) | OSS platform | Semrush/Ahrefs alternative | 🟢 | keyword-research, seo-audit, serp-analysis |
| advertools (1.4k) | Python lib | SEO productivity, SERP, sitemaps | 🟢 | technical-seo, keyword-research |
| Search Console API | Google API | Index coverage, queries | 🟡 | technical-seo, seo-audit |

### Web research (ungated, powers intelligence)

| Tool | Covers | Gate | Skills served |
|---|---|---|---|
| Agent Reach / web-search MCP | public internet | 🟢 | market-sizing, competitor-audit, trend-detection, ad-library-research, social-listening, demand-analysis |
| Browser automation (CDP/Playwright) | render-heavy pages, ad libraries | 🟢 read / 🟡 write | ad-library-research, technology-analysis, serp-analysis |

---

## Wiring priority (what to install first)

1. **Web research** (ungated) — unblocks the entire intelligence layer immediately. No credentials.
2. **markifact-mcp** or **google-ads-mcp** (read-only first) — unblocks paid reporting.
3. **Search Console API** — unblocks technical SEO + keyword data.
4. **GA4 MCP** — unblocks funnel/analytics reads.
5. Then, and only then, graduated write access behind 🔴 gates.

## What's blocked on credentials

Nothing in this layer can be turned on without account auth: Google Ads, Meta, LinkedIn, TikTok ad accounts; GA4; Search Console; CRM. The wiring map is ready; the credentials are yours to supply when Collision's runtime connects to a customer's stack.

## Runtime note

These SKILL.md files are runtime-agnostic — they run in Hermes, Claude Code, or Collision's own harness. The agent layer in `agents/agent-layer.md` maps skills → specialists; this file maps skills → tools. Wire both and the system transitions from reference to operator.
