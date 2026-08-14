# Marketing OS — Agent Layer

Specialized agents that orchestrate the skills. Each agent is a role with a defined remit, the skills it owns, its routing, and its gates. When the Marketing OS is wired to a runtime (Hermes, Claude Code, or a custom harness), these become executable agent definitions; until then they are the canonical orchestration map.

## Design principles
- **One agent, one decision surface.** Directors decide; specialists execute; critics review.
- **Read-only by default.** Any agent that can spend money, publish, or mutate a CRM/external system runs behind a capability gate (see `execution/mcp-map.md`).
- **Skills are shared, agents are views.** Multiple agents may load the same skill; the agent supplies the brief and the authority level.

---

## Paid Media Director

Owns: paid acquisition outcomes (ROAS, CAC, budget allocation). Decides where money goes.

| Specialist | Skills loaded | Remit |
|---|---|---|
| Google Ads Agent | google-ads, shopping-feeds, media-planning | Search/Shopping/PMax/Display/YouTube architecture, bidding, audits |
| Meta Ads Agent | meta-ads, creative-testing, ugc-advertising | FB/IG campaigns, Advantage+, creative volume |
| LinkedIn Ads Agent | linkedin-ads, account-intelligence | ABM, Sponsored Content, lead gen forms |
| TikTok Ads Agent | tiktok-ads, ugc-advertising | Spark Ads, Shop, creative-first |
| Amazon Ads Agent | amazon-ads, marketplace-expansion, shopping-feeds | SP/SB/SD, ACoS, listing synergy |
| Programmatic Agent | programmatic-ctv, native-ads, retail-media | DSP, CTV, native, retail media networks |
| Creative Intelligence Agent | ad-creative-generator, hook-frameworks, ad-library-research, creative-testing | Angles, hooks, competitor creative mining, testing |
| Attribution Agent | mmm-incrementality, attribution-model-selection, performance-reporting | Incrementality, MMM, blended reporting |
| Budget Optimization Agent | media-planning, performance-reporting, benchmark-frameworks | Cross-platform allocation, portfolio mix |
| Paid Media Critic | (review role) all paid skills | Red-team every campaign plan before launch |

**Gates:** any budget change, campaign launch, or bid edit requires human approval. Read-only analytics and planning are ungated.

---

## SEO Director

Owns: organic + AI-search visibility (traffic, rankings, citations).

| Specialist | Skills loaded | Remit |
|---|---|---|
| Technical SEO Agent | technical-seo, seo-audit, international-seo | Crawl, index, CWV, JS, schema, hreflang |
| Content SEO Agent | keyword-research, serp-analysis, content-strategy | Topical authority, clusters, intent |
| Local SEO Agent | local-seo | GBP, citations, reviews |
| Enterprise SEO Agent | technical-seo, programmatic-seo, international-seo | Scale SEO, migrations, multi-region |
| Ecommerce SEO Agent | shopping-feeds, keyword-research, programmatic-seo | PDP, category, feeds |
| GEO Agent | entity-optimization, ai-citation-acquisition, ai-answer-tracking | AI visibility, citations, share-of-voice |
| Backlink Agent | link-building | Digital PR, prospecting, anchors |
| Keyword Agent | keyword-research, serp-analysis | Research, clustering, intent mapping |
| SERP Agent | serp-analysis | Feature landscape, snippet opportunity |
| SEO Critic | (review role) all SEO skills | Red-team audits before implementation |

**Gates:** content publication and link outreach are gated; research/audit are ungated.

---

## Demand & Lifecycle Director

Owns: outbound pipeline and lifecycle revenue.

| Specialist | Skills loaded | Remit |
|---|---|---|
| Outbound Agent | cold-email-sequence, lead-sourcing-enrichment, multichannel-outbound | Sequences, list building, cadence |
| Deliverability Agent | email-deliverability, domain-reputation-ops, reply-classification | Auth, warming, reputation, classification |
| Lifecycle Agent | lifecycle-sequences, newsletter-operations, email-copy | Onboarding, retention, winback |
| CRM Agent | crm-lead-ops, crm-pipeline-attribution, workflow-builder | Routing, scoring, attribution |

**Gates:** sending to real humans, list purchases, domain rotation changes are gated.

---

## Brand & Content Director

Owns: positioning, messaging, content, PR, community.

| Specialist | Skills loaded | Remit |
|---|---|---|
| Positioning Agent | positioning-framework, value-proposition, messaging-hierarchy, category-design | Differentiation, messaging |
| Copy Agent | conversion-copywriting, landing-page-copy, ad-copy, email-copy, video-scripts | All copy surfaces |
| Content Agent | content-strategy, content-calendar, content-repurposing, thought-leadership | Editorial, repurposing |
| PR Agent | pr-strategy, press-pitching, press-release, newsjacking | Earned media |
| Launch Agent | product-launch-playbook, product-hunt-launch, events-webinars | Launch orchestration |
| Partnerships Agent | partnership-strategy, co-marketing, affiliate-program, referral-program, influencer-marketing, creator-outreach, ambassador-program | Partner/creator economy |

**Gates:** publishing, pitching journalists, and public statements are gated.

---

## Growth & Intelligence Director

Owns: measurement, experimentation, research.

| Specialist | Skills loaded | Remit |
|---|---|---|
| Research Agent | market-sizing, demand-analysis, intent-signals, customer-research, competitor-audit, win-loss-analysis | Market/customer/competitor research |
| Experimentation Agent | ab-testing, experiment-prioritization, experimentation-program | Test design, velocity, learning library |
| Analytics Agent | analytics-setup, funnel-analysis, product-analytics, dashboard-design | Measurement infrastructure |
| CRO Agent | cro-audit, landing-page-optimization, signup-flow, checkout-optimization, forms-microcopy | Conversion optimization |
| Ops Agent | utm-governance, workflow-builder, benchmark-frameworks | Marketing operations |

**Gates:** instrumenting production (GTM/GA4 changes), shipping CRO changes are gated.

---

## Composition example (spec §35 north star)

"Launch this product in the US" decomposes as:

```
Brand & Content Director (positioning, messaging)
  → Growth & Intelligence (market + customer + competitor research, ICP)
  → Brand & Content (offer, landing page, content)
  → SEO Director (SEO + GEO)
  → Demand & Lifecycle (email, outbound, lifecycle)
  → Paid Media Director (ads + creative)
  → Partnerships Agent (creators, affiliates)
  → Launch Agent (launch orchestration)
  → Growth & Intelligence (analytics, attribution, CRO, experimentation)
```
