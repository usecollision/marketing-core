# Dependency Graph

## Core Dependency (all repos depend on this)
- marketing-core (context, ontology, frameworks, routing)

## Layer 1: Strategy & Intelligence (inputs to everything)
- marketing-intelligence (strategy + research + intelligence) → depends on: marketing-core
  - skills: growth-strategy, gtm-plan, icp-builder, positioning-framework, customer-research, reddit-research, review-mining, competitor-audit
  - wave-1: market-sizing, customer-interviews, survey-design, social-listening, trend-detection, pricing-intelligence, competitor-battlecards, account-intelligence

## Layer 2: Messaging & Content (consumes research, feeds channels)
- marketing-messaging (copy + content) → depends on: marketing-core, marketing-intelligence
  - skills: conversion-copywriting, landing-page-copy, content-strategy
  - wave-1: brand-voice, value-proposition, messaging-hierarchy, customer-language-bank, objection-handling, email-copy, case-study-builder, sales-deck, video-scripts

## Layer 3: Channels (execution layer)
- marketing-channels (seo + ai-search + social + email + outbound) → depends on: marketing-core, marketing-intelligence, marketing-messaging
  - skills: keyword-research, seo-audit, ai-search-audit, linkedin-content, social-strategy, lifecycle-sequences, cold-email-sequence
  - wave-1: technical-seo, link-building, programmatic-seo, local-seo, serp-analysis, entity-optimization, content-calendar, reddit-engagement, youtube-strategy, community-strategy
- marketing-paid (paid + ad-creative + ecommerce) → depends on: marketing-core, marketing-intelligence, marketing-messaging
  - skills: paid-strategy, meta-ads, ad-creative-generator, hook-frameworks, shopify-marketing-audit
  - wave-1: google-ads, linkedin-ads, tiktok-ads, amazon-ads, reddit-ads, media-planning, creative-testing, performance-reporting

## Layer 4: Optimization (improves channels)
- marketing-optimize (analytics + attribution + cro + automation) → depends on: marketing-core
  - skills: metrics-framework, attribution-model-selection, cro-audit, workflow-builder
  - wave-1: analytics-setup, funnel-analysis, landing-page-optimization, signup-flow, ab-testing, experiment-prioritization, mmm-incrementality

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
4. marketing-channels (launch content, social, email)
5. marketing-paid (launch ads)
6. marketing-optimize (tracking setup, CRO)

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
5. marketing-optimize (pipeline tracking)

### Path: Paid Acquisition Scale
1. marketing-core (load context)
2. marketing-intelligence (channel strategy, budget, ICP)
3. marketing-paid (paid-strategy, ad-creative, meta-ads)
4. marketing-messaging (landing page copy)
5. marketing-optimize (attribution, ROAS tracking)

## Roadmap Skills (referenced but not yet built)
- marketing-optimize/analytics-setup, marketing-optimize/funnel-analysis, marketing-optimize/landing-page-optimization, marketing-optimize/signup-flow
- marketing-messaging/email-copy
- marketing-channels/content-calendar, marketing-channels/reddit-engagement
- marketing-paid/google-ads-audit
