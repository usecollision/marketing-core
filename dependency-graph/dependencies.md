# Dependency Graph

## Core Dependency (all repos depend on this)
- marketing-core (context, ontology, frameworks, routing)

## Layer 1: Strategy & Intelligence (inputs to everything)
- marketing-intelligence (strategy + research + intelligence) → depends on: marketing-core
  - skills (29): growth-strategy, gtm-plan, icp-builder, positioning-framework, customer-research, reddit-research, review-mining, competitor-audit, market-sizing, customer-interviews, survey-design, social-listening, trend-detection, pricing-intelligence, competitor-battlecards, account-intelligence, market-map, demand-analysis, intent-signals, ad-library-research, technology-analysis, personas, win-loss-analysis, pricing-packaging-strategy, industry-category-analysis, market-forecasting, support-ticket-mining, call-transcript-analysis, category-design

## Layer 2: Messaging & Content (consumes research, feeds channels)
- marketing-messaging (copy + content) → depends on: marketing-core, marketing-intelligence
  - skills (17): conversion-copywriting, landing-page-copy, content-strategy, brand-voice, value-proposition, messaging-hierarchy, customer-language-bank, objection-handling, email-copy, case-study-builder, sales-deck, video-scripts, ad-copy, thought-leadership, content-repurposing, offer-design, localization

## Layer 3: Channels (execution layer)
- marketing-channels (seo + ai-search + social + email + outbound + pr + launches + events + partnerships + creators) → depends on: marketing-core, marketing-intelligence, marketing-messaging
  - skills (44): keyword-research, seo-audit, ai-search-audit, linkedin-content, social-strategy, lifecycle-sequences, cold-email-sequence, technical-seo, link-building, programmatic-seo, local-seo, serp-analysis, entity-optimization, content-calendar, reddit-engagement, youtube-strategy, community-strategy, pr-strategy, press-pitching, press-release, newsjacking, product-launch-playbook, product-hunt-launch, podcast-appearances, events-webinars, partnership-strategy, co-marketing, affiliate-program, referral-program, influencer-marketing, creator-outreach, ambassador-program, email-deliverability, newsletter-operations, lead-sourcing-enrichment, multichannel-outbound, reply-classification, domain-reputation-ops, x-twitter-growth, instagram-tiktok-organic, international-seo, ai-citation-acquisition, ai-answer-tracking, pinterest-threads
- marketing-paid (paid + ad-creative + ecommerce) → depends on: marketing-core, marketing-intelligence, marketing-messaging
  - skills (27): paid-strategy, meta-ads, ad-creative-generator, hook-frameworks, shopify-marketing-audit, google-ads, linkedin-ads, tiktok-ads, amazon-ads, reddit-ads, media-planning, creative-testing, performance-reporting, microsoft-ads, x-ads, apple-search-ads, pinterest-ads, snapchat-ads, quora-ads, native-ads, programmatic-ctv, spotify-ads, podcast-newsletter-ads, marketplace-expansion, shopping-feeds, ugc-advertising, retail-media

## Layer 4: Optimization (improves channels)
- marketing-optimize (analytics + attribution + cro + automation) → depends on: marketing-core
  - skills (20): metrics-framework, attribution-model-selection, cro-audit, workflow-builder, analytics-setup, funnel-analysis, landing-page-optimization, signup-flow, ab-testing, experiment-prioritization, mmm-incrementality, checkout-optimization, forms-microcopy, product-analytics, dashboard-design, crm-pipeline-attribution, benchmark-frameworks, utm-governance, experimentation-program, crm-lead-ops

## Feedback Loops
- marketing-optimize → feeds back into → marketing-intelligence (performance data → strategy)
- marketing-intelligence → feeds back into → marketing-intelligence (market shifts → strategy)
- marketing-optimize (cro) → feeds back into → marketing-messaging (winning copy patterns)
- marketing-optimize (attribution) → feeds back into → marketing-paid (budget allocation)
- marketing-intelligence (competitor intel) → feeds back into → marketing-intelligence (competitive moves)

## Execution Paths

### Path: New Product Launch
1. marketing-core (load context)
2. marketing-intelligence (positioning, ICP, research validation)
3. marketing-messaging (messaging, landing page copy)
4. marketing-channels (pr-strategy, product-launch-playbook, product-hunt-launch)
5. marketing-channels (launch content, social, email)
6. marketing-paid (launch ads)
7. marketing-optimize (tracking setup, CRO)

### Path: SEO Growth Engine
1. marketing-core (load context)
2. marketing-channels (seo-audit, keyword-research, ai-search-audit)
3. marketing-messaging (content strategy, page copy)
4. marketing-optimize (analytics, CRO)

### Path: Outbound Revenue Engine
1. marketing-core (load context)
2. marketing-intelligence (prospect research, competitor positioning)
3. marketing-messaging (email copy, personalization)
4. marketing-channels (cold-email-sequence, social outreach)
5. marketing-optimize (pipeline tracking, crm-pipeline-attribution)

### Path: Paid Acquisition Scale
1. marketing-core (load context)
2. marketing-intelligence (channel strategy, budget, ICP)
3. marketing-paid (paid-strategy, media-planning, platform skills, creative-testing)
4. marketing-messaging (landing page copy)
5. marketing-optimize (attribution, mmm-incrementality, performance reporting)

### Path: PR & Authority
1. marketing-core (load context)
2. marketing-intelligence (positioning, trend-detection)
3. marketing-channels (pr-strategy, press-pitching, press-release, newsjacking)
4. marketing-channels (podcast-appearances, events-webinars)
5. marketing-optimize (share of voice, referral tracking)

## Roadmap Skills (referenced but not yet built)
None — all referenced skills exist. Next expansion targets are listed in capability-catalog.md (wave-3 planned).
