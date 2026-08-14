# AGENTS.md - Marketing OS Agent Instructions

## Overview
This file instructs AI agents on how to navigate, discover, and chain skills across the UseCollision Marketing OS.

## Context Loading (Always First)
Before executing ANY marketing skill:
1. Read context/product-marketing.md for product, ICP, positioning
2. Read context/project-context.md for current goals and constraints
3. Check the skill's required_context field for additional files

## Skill Discovery
Skills live in domain repos under usecollision/marketing-*. Each skill is a SKILL.md file following the template in templates/SKILL-TEMPLATE.md.

To find the right skill:
1. Match user intent to skill triggers in frontmatter
2. Check category field for domain alignment
3. Review related_skills for chaining opportunities

## Routing Logic

### Router Command: /marketing-do
When a user says /marketing-do [task], route as follows:

| Intent Pattern | Route To |
|---------------|----------|
| strategy, GTM, positioning, ICP, pricing, research, customer, interview, Reddit mining, competitor, competitive, spy, benchmark | marketing-intelligence |
| copy, headline, landing page copy, CTA, content, blog, newsletter, case study | marketing-messaging |
| SEO, keywords, technical, backlinks, sitemap, AI search, AEO, GEO, LLMO, entity, social, LinkedIn post, tweet, thread, cold email, outbound, sequence, prospecting, lifecycle, onboarding, nurture, retention email | marketing-channels |
| ads, paid, Meta, Google Ads, campaign budget, ad creative, hooks, UGC, carousel, video ad, Shopify, DTC, ecommerce, Amazon, PDP | marketing-paid |
| CRO, conversion, A/B test, landing page opt, analytics, GA4, metrics, dashboard, funnel, attribution, MMM, incrementality, tracking, automation, workflow, n8n, Zapier, MCP | marketing-optimize |

### Multi-Skill Flows
Common chained workflows:

**New product launch:**
marketing-intelligence (positioning, ICP, research) → marketing-messaging (messaging, content) → marketing-paid (launch ads) → marketing-channels (social, email) → marketing-optimize (tracking)

**SEO overhaul:**
marketing-channels (seo-audit, ai-search-audit) → marketing-messaging (content plan, page copy) → marketing-optimize (tracking, CRO)

**Outbound campaign:**
marketing-intelligence (prospect research, competitor intel) → marketing-messaging (email copy) → marketing-channels (outbound sequences) → marketing-optimize (tracking)

**Growth optimization:**
marketing-optimize (funnel analysis, conversion audit) → marketing-messaging (copy improvements) → marketing-paid (ad optimization) → marketing-optimize (measurement)

## Dependency Rules
- Never execute a channel skill (paid, social, outbound, email) without first confirming product-marketing context exists
- Strategy and research skills feed INTO execution skills, not the reverse
- Analytics and attribution skills should be invoked AFTER execution, not before
- CRO skills require existing pages/funnels to optimize

## Skill Execution Protocol
1. Load required context
2. Execute workflow steps in order
3. Respect gates (don't skip to next step without meeting criteria)
4. Produce outputs in the format specified by the skill
5. Update project-context.md with results if skill modifies strategy or goals
6. Suggest related_skills for next steps

## Quality Standards
- All outputs must reference the brand voice from product-marketing.md
- Quantitative claims need data sources cited
- Recommendations must be actionable (not just strategic advice)
- Each skill execution should produce artifacts the user can immediately use
