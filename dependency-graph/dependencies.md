# Dependency Graph

## Core Dependencies (all repos depend on these)
- marketing-core (context, ontology, frameworks, routing)

## Layer 1: Strategy & Intelligence (inputs to everything)
- marketing-strategy → depends on: marketing-core
- marketing-research → depends on: marketing-core, marketing-strategy
- marketing-intelligence → depends on: marketing-core, marketing-research

## Layer 2: Messaging & Content (consumes research, feeds channels)
- marketing-copy → depends on: marketing-core, marketing-strategy, marketing-research
- marketing-content → depends on: marketing-core, marketing-strategy, marketing-copy

## Layer 3: Channels (execution layer)
- marketing-seo → depends on: marketing-core, marketing-content, marketing-copy
- marketing-ai-search → depends on: marketing-core, marketing-seo, marketing-content
- marketing-paid → depends on: marketing-core, marketing-strategy, marketing-copy, marketing-ad-creative
- marketing-ad-creative → depends on: marketing-core, marketing-copy, marketing-research
- marketing-social → depends on: marketing-core, marketing-content, marketing-copy
- marketing-outbound → depends on: marketing-core, marketing-research, marketing-copy, marketing-intelligence
- marketing-email → depends on: marketing-core, marketing-copy, marketing-strategy

## Layer 4: Optimization (improves channels)
- marketing-cro → depends on: marketing-core, marketing-copy, marketing-analytics
- marketing-analytics → depends on: marketing-core
- marketing-attribution → depends on: marketing-core, marketing-analytics

## Layer 5: Verticals & Automation
- marketing-ecommerce → depends on: marketing-core, marketing-paid, marketing-email, marketing-cro
- marketing-automation → depends on: marketing-core, marketing-analytics

## Feedback Loops
- marketing-analytics → feeds back into → marketing-strategy (performance data)
- marketing-research → feeds back into → marketing-strategy (market shifts)
- marketing-cro → feeds back into → marketing-copy (winning copy patterns)
- marketing-attribution → feeds back into → marketing-paid (budget allocation)
- marketing-intelligence → feeds back into → marketing-strategy (competitive moves)

## Execution Paths

### Path: New Product Launch
1. marketing-core (load context)
2. marketing-strategy (positioning, ICP)
3. marketing-research (validate ICP, find channels)
4. marketing-copy (messaging, landing page)
5. marketing-content (launch content)
6. marketing-paid (launch ads)
7. marketing-social (launch posts)
8. marketing-outbound (launch outreach)
9. marketing-analytics (tracking setup)
10. marketing-cro (optimize conversion)

### Path: SEO Growth Engine
1. marketing-core (load context)
2. marketing-seo (audit, keyword research)
3. marketing-ai-search (AI visibility)
4. marketing-content (content plan, production)
5. marketing-copy (page optimization)
6. marketing-cro (conversion optimization)
7. marketing-analytics (tracking, dashboards)

### Path: Outbound Revenue Engine
1. marketing-core (load context)
2. marketing-research (prospect research)
3. marketing-intelligence (competitor positioning)
4. marketing-copy (email copy, personalization)
5. marketing-outbound (sequences, multi-channel)
6. marketing-analytics (pipeline tracking)

### Path: Paid Acquisition Scale
1. marketing-core (load context)
2. marketing-strategy (channel strategy, budget)
3. marketing-ad-creative (creative production)
4. marketing-paid (campaign setup, optimization)
5. marketing-cro (landing page optimization)
6. marketing-analytics (ROAS tracking)
7. marketing-attribution (channel contribution)