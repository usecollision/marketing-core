# Marketing OS — Capability Universe

The canonical map of everything the Marketing OS can do. Repository → domain → capability → sub-capability, with platform/workflow coverage and OSS reuse targets.

**Status legend:** ✅ LIVE · 🗓 PLANNED (wave 2+)

Generated from the capability-expansion research pass. Companion: `research/oss-landscape.md` (OSS discovery, 24 domains, ~190 repos).

---

## marketing-core — Kernel

| Capability | Status | Notes |
|---|---|---|
| Product/brand context templates | ✅ | context/product-marketing.md |
| Universal frameworks (AARRR, JTBD, etc.) | ✅ | frameworks/ |
| Ontology & taxonomy | ✅ | ontology/ (updated with this pass) |
| SKILL template & folder spec | ✅ | templates/ |
| Routing logic & agent instructions | ✅ | AGENTS.md |
| Dependency graph | ✅ | dependency-graph/ |
| Capability catalog (this file) | ✅ | — |

---

## marketing-intelligence — Understand

### Market research
| Capability | Status | Sub-capabilities |
|---|---|---|
| market-sizing | ✅ | TAM/SAM/SOM, top-down, bottom-up, segment sizing |
| market-map | 🗓 | category mapping, competitor positioning map |
| market-trends | ✅ | trend-detection, durability validation, signal sources |
| industry/category analysis | 🗓 | Porter's 5F, category lifecycle |
| demand analysis | 🗓 | search demand, review velocity, Google Trends |
| market forecasting | 🗓 | growth projections, scenario modeling |

### Customer research
| Capability | Status | Sub-capabilities |
|---|---|---|
| customer-research | ✅ | pain points, language, buying triggers |
| customer-interviews | ✅ | interview design, recruiting, synthesis |
| survey-design | ✅ | questionnaire bias, NPS/CSAT, response analysis |
| reddit-research | ✅ | pain mining, subreddit discovery |
| review-mining | ✅ | G2/App Store/Amazon/Capterra/TrustRadius |
| social-listening | ✅ | brand mentions, sentiment, conversation mining |
| support-ticket mining | 🗓 | Zendesk/Intercom log analysis |
| call-transcript analysis | 🗓 | Gong/Chorus mining |

### Competitive intelligence
| Capability | Status | Sub-capabilities |
|---|---|---|
| competitor-audit | ✅ | positioning, messaging, content, SEO, ads, product |
| competitor-battlecards | ✅ | win/loss plays, objection rebuttals |
| pricing-intelligence | ✅ | pricing teardowns, WTP estimation |
| ad-library research | 🗓 | Meta/Google ad library mining |
| technology analysis | 🗓 | BuiltWith/stack fingerprinting |

### Audience intelligence
| Capability | Status | Sub-capabilities |
|---|---|---|
| icp-builder | ✅ | segmentation, validation |
| account-intelligence | ✅ | firmographics, technographics, funding signals (ABM) |
| personas | 🗓 | persona assembly from research |
| intent signals | 🗓 | G2 intent, review velocity, job-change triggers |

### Strategy & GTM
| Capability | Status | Sub-capabilities |
|---|---|---|
| growth-strategy | ✅ | growth model, channels, loops |
| gtm-plan | ✅ | GTM for launch/expansion |
| positioning-framework | ✅ | April Dunford methodology |
| pricing & packaging strategy | 🗓 | price design, packaging, monetization |

---

## marketing-messaging — Create

### Brand & positioning
| Capability | Status | Sub-capabilities |
|---|---|---|
| brand-voice | ✅ | voice guide, tone matrix, do/don't examples |
| value-proposition | ✅ | JTBD-based value props, USP |
| messaging-hierarchy | ✅ | positioning → pillars → proof points → taglines |
| customer-language-bank | ✅ | verbatim phrases by stage/pain |

### Copywriting
| Capability | Status | Sub-capabilities |
|---|---|---|
| conversion-copywriting | ✅ | any-surface copy frameworks |
| landing-page-copy | ✅ | hero → features → proof → objection → CTA |
| email-copy | ✅ | subject lines, preview, body, CTA |
| ad-copy | 🗓 | paid media copy (see marketing-paid hooks) |
| objection-handling | ✅ | rebuttals, pre-emptive copy |
| video-scripts | ✅ | short-form hooks, retain, payoff |

### Content & proof
| Capability | Status | Sub-capabilities |
|---|---|---|
| content-strategy | ✅ | organic traffic, authority |
| case-study-builder | ✅ | challenge-solution-results narrative |
| sales-deck | ✅ | pitch narrative, slide-by-slide |
| thought leadership | 🗓 | POV essays, founder content |
| content repurposing | 🗓 | 1-to-N asset workflow |

---

## marketing-channels — Distribute

### SEO
| Capability | Status | Sub-capabilities |
|---|---|---|
| keyword-research | ✅ | topical authority, clustering |
| seo-audit | ✅ | 5-pillar audit |
| technical-seo | ✅ | crawl, index, CWV, JS, log files, schema |
| link-building | ✅ | prospecting, digital PR, anchors |
| programmatic-seo | ✅ | templates, data sources, thin-content risk |
| local-seo | ✅ | GBP, citations, reviews |
| serp-analysis | ✅ | features, intent, opportunity |
| international/enterprise SEO | 🗓 | hreflang, multi-region |

### AI search (GEO/AEO)
| Capability | Status | Sub-capabilities |
|---|---|---|
| ai-search-audit | ✅ | ChatGPT/Perplexity/Claude/Gemini visibility |
| entity-optimization | ✅ | entity extraction, knowledge graph, citations |
| AI citation acquisition | 🗓 | source placement, wiki/data citations |
| AI answer tracking | 🗓 | monitoring tools, share-of-voice |

### Social (per-platform)
| Capability | Status | Sub-capabilities |
|---|---|---|
| social-strategy | ✅ | cross-platform strategy |
| linkedin-content | ✅ | personal + company brand |
| reddit-engagement | ✅ | community participation, compliance |
| youtube-strategy | ✅ | channel, SEO, retention, formats |
| community-strategy | ✅ | Discord/Telegram/Slack, flywheel |
| X/Twitter growth | 🗓 | threads, engagement |
| Instagram/TikTok organic | 🗓 | Reels/Shorts formats |
| Pinterest/Threads | 🗓 | platform playbooks |

### PR, launches & events
| Capability | Status | Sub-capabilities |
|---|---|---|
| pr-strategy | 🔨 | narrative, target publications, angles, SOV |
| press-pitching | 🔨 | media lists, angle-matching, follow-up |
| press-release | 🔨 | newswire format, distribution, timing |
| newsjacking | 🔨 | rapid response, safe hooks |
| product-launch-playbook | 🔨 | runbook, sequencing, measurement |
| product-hunt-launch | 🔨 | PH + HN + BetaList + directories |
| podcast-appearances | 🔨 | show discovery, pitching, promos |
| events-webinars | 🔨 | format, promotion, follow-up |

### Email & lifecycle
| Capability | Status | Sub-capabilities |
|---|---|---|
| lifecycle-sequences | ✅ | onboarding → retention → winback |
| content-calendar | ✅ | editorial planning, cadence |
| deliverability | 🗓 | SPF/DKIM/DMARC, warming, reputation |
| newsletter operations | 🗓 | format, growth, engagement |

### Outbound
| Capability | Status | Sub-capabilities |
|---|---|---|
| cold-email-sequence | ✅ | sequences, personalization |
| lead sourcing/enrichment | 🗓 | list building, data providers |
| multichannel outbound | 🗓 | email + LinkedIn + calls orchestration |
| reply classification | 🗓 | positive/negative/objection routing |
| domain reputation ops | 🗓 | rotation, warmup, scaling |

---

## marketing-paid — Demand

### Cross-platform intelligence
| Capability | Status | Sub-capabilities |
|---|---|---|
| paid-strategy | ✅ | platform selection, funnel design |
| media-planning | ✅ | budget allocation, channel mix ("₹10 lakh → where?") |
| performance-reporting | ✅ | cross-platform rollups, blended CAC/ROAS |
| incrementality & MMM | ✅ (in optimize) | geo tests, holdouts, MMM |

### Platform execution
| Platform | Status | Coverage depth |
|---|---|---|
| Meta (FB/IG) | ✅ | setup, structure, optimization |
| Google Ads | ✅ | Search/Shopping/PMax/Display/YouTube |
| LinkedIn Ads | ✅ | Sponsored/TLA/Conversation, ABM targeting |
| TikTok Ads | ✅ | Spark, ecommerce, creative-led |
| Reddit Ads | ✅ | community-native creative, placements |
| Amazon Ads | ✅ | SP/SB/SD, ACoS, listing synergy |
| X/Twitter Ads | 🗓 | — |
| Pinterest Ads | 🗓 | — |
| Microsoft Ads | 🗓 | — |
| Apple Search Ads | 🗓 | — |
| Snapchat Ads | 🗓 | — |
| Quora Ads | 🗓 | — |
| Spotify Ads | 🗓 | — |
| Native (Taboola/Outbrain) | 🗓 | — |
| Programmatic/CTV | 🗓 | DSPs, retargeting |

### Creative intelligence
| Capability | Status | Sub-capabilities |
|---|---|---|
| ad-creative-generator | ✅ | angles, formats, platforms |
| hook-frameworks | ✅ | scroll-stoppers, patterns |
| creative-testing | ✅ | testing design, fatigue detection, scoring |
| UGC & creator briefs | 🗓 | brief generation, creator outreach |
| ad library research | 🗓 | competitor creative mining |

### Ecommerce
| Capability | Status | Sub-capabilities |
|---|---|---|
| shopify-marketing-audit | ✅ | conversion, retention, growth |
| marketplace expansion | 🗓 | Amazon/Flipkart/other marketplaces |
| feeds & Merchant Center | 🗓 | shopping feeds, GMC health |

---

## marketing-optimize — Improve

### Analytics
| Capability | Status | Sub-capabilities |
|---|---|---|
| metrics-framework | ✅ | stage-appropriate metrics |
| analytics-setup | ✅ | GA4/GTM, event taxonomy, tracking plans |
| funnel-analysis | ✅ | stage-by-stage drop-off diagnosis |
| product analytics | 🗓 | Mixpanel/Amplitude/PostHog |
| dashboard design | 🗓 | exec dashboards, self-serve |

### Attribution
| Capability | Status | Sub-capabilities |
|---|---|---|
| attribution-model-selection | ✅ | model choice by maturity |
| mmm-incrementality | ✅ | geo experiments, holdouts, MMM |
| CRM/pipeline attribution | 🗓 | lead → revenue mapping |

### CRO
| Capability | Status | Sub-capabilities |
|---|---|---|
| cro-audit | ✅ | friction, drop-offs, opportunities |
| landing-page-optimization | ✅ | LP-specific optimization |
| signup-flow | ✅ | signup/onboarding conversion |
| checkout optimization | 🗓 | payments, address, one-click |
| forms & microcopy | 🗓 | — |

### Experimentation
| Capability | Status | Sub-capabilities |
|---|---|---|
| ab-testing | ✅ | design, significance, sample size |
| experiment-prioritization | ✅ | ICE/RICE/PIE/PXL |
| experimentation program | 🗓 | velocity, learning library |

### Automation & ops
| Capability | Status | Sub-capabilities |
|---|---|---|
| workflow-builder | ✅ | n8n/Zapier/Make, MCP |
| CRM & lead ops | 🗓 | routing, scoring, lifecycle stages |
| UTM & campaign ops | 🗓 | taxonomy, governance |
| calendar & planning | ✅ | content-calendar (in channels) |

---

## Cross-repository composition

Canonical chain: **competitor research → creative intelligence → positioning → messaging → paid → landing page → CRO → analytics → attribution → optimization**

North-star objective decomposition (e.g. "Launch this product in the US") is supported by the dependency graph in `dependency-graph/dependencies.md`.

## OSS reuse targets (top picks from research/oss-landscape.md)

| Repo | Stars | What to reuse/adapt |
|---|---|---|
| coreyhaines31/marketingskills | 44k | upstream we already normalize from |
| AgriciDaniel/claude-seo | 14k | 25 SEO sub-skills + 18 sub-agents — technical SEO, GEO |
| AgriciDaniel/claude-ads | 8k | 12-platform paid ops — platform skill decomposition |
| every-app/open-seo | 11.8k | OSS Semrush/Ahrefs alternative (tooling) |
| zubair-trabzada/geo-seo-claude | 9.3k | citability scoring, GEO-first approach |
| aaron-he-zhu/aaron-marketing-skills | 2.5k | 120 skills across 7 disciplines — coverage map |
| ericosiu/ai-marketing-skills | 3.4k | growth experiments, pipeline, outbound |
| indranilbanerjee/digital-marketing-pro | 736 | OS architecture (strategy→analytics) |
| OpenClaudia/openclaudia-skills | 633 | 34 skills — content, email, ads |
| googleads/google-ads-mcp | 854 | Google Ads MCP server (execution layer) |
| pipeboard-co/meta-ads-mcp | 1.2k | Meta Ads MCP server |
| markifact/markifact-mcp | 45 | 5-platform ads MCP (300+ operations) |
| twentyhq/twenty | 55k | OSS CRM (execution backend) |
| mautic/mautic | 10k | OSS marketing automation |
| listmonk | 22.8k | OSS newsletter (email ops backend) |
| snowplow/snowplow | 7k | customer data infra (analytics backend) |
