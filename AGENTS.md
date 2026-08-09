# AGENTS.md - Marketing OS Agent Instructions

## Overview
This file instructs AI agents on how to navigate, discover, and chain skills across the UseCollision Marketing OS.

## Context Loading (Always First)
Before executing ANY marketing skill:
1. Read context/product-marketing.md for product, ICP, positioning
2. Read context/project-context.md for current goals and constraints
3. Check the skill's equired_context field for additional files

## Skill Discovery
Skills live in domain repos under usecollision/marketing-*. Each skill is a SKILL.md file following the template in 	emplates/SKILL-TEMPLATE.md.

To find the right skill:
1. Match user intent to skill 	riggers in frontmatter
2. Check category field for domain alignment
3. Review elated_skills for chaining opportunities

## Routing Logic

### Router Command: /marketing-do
When a user says /marketing-do [task], route as follows:

| Intent Pattern | Route To |
|---------------|----------|
| strategy, GTM, positioning, ICP, pricing | marketing-strategy |
| research, customer, interview, Reddit mining | marketing-research |
| competitor, competitive, spy, benchmark | marketing-intelligence |
| SEO, keywords, technical, backlinks, sitemap | marketing-seo |
| AI search, AEO, GEO, LLMO, entity | marketing-ai-search |
| ads, paid, Meta, Google Ads, campaign budget | marketing-paid |
| ad creative, hooks, UGC, carousel, video ad | marketing-ad-creative |
| content, blog, newsletter, case study | marketing-content |
| copy, headline, landing page copy, CTA | marketing-copy |
| social, LinkedIn post, tweet, thread | marketing-social |
| cold email, outbound, sequence, prospecting | marketing-outbound |
| lifecycle, onboarding, nurture, retention email | marketing-email |
| CRO, conversion, A/B test, landing page opt | marketing-cro |
| analytics, GA4, metrics, dashboard, funnel | marketing-analytics |
| attribution, MMM, incrementality, tracking | marketing-attribution |
| Shopify, DTC, ecommerce, Amazon, PDP | marketing-ecommerce |
| automation, workflow, n8n, Zapier, MCP | marketing-automation |

### Multi-Skill Flows
Common chained workflows:

**New product launch:**
marketing-strategy (positioning) → marketing-research (ICP validation) → marketing-copy (messaging) → marketing-content (launch content) → marketing-paid (launch ads) → marketing-social (launch posts) → marketing-analytics (tracking)

**SEO overhaul:**
marketing-seo (audit) → marketing-ai-search (AI visibility) → marketing-content (content plan) → marketing-copy (page copy) → marketing-analytics (tracking) → marketing-cro (conversion)

**Outbound campaign:**
marketing-research (prospect research) → marketing-intelligence (competitor intel) → marketing-copy (email copy) → marketing-outbound (sequences) → marketing-analytics (tracking)

**Growth optimization:**
marketing-analytics (funnel analysis) → marketing-cro (conversion audit) → marketing-copy (copy improvements) → marketing-paid (ad optimization) → marketing-attribution (measurement)

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