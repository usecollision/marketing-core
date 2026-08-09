# Marketing OS Ontology

## Capability Taxonomy

### Strategy & GTM
- Marketing Strategy
- Go-To-Market (GTM)
- Positioning & Messaging
- ICP & Segmentation
- Category Design
- Growth Strategy
- Channel Strategy
- Product Marketing
- PLG / SLG / FLG
- Growth Loops
- Marketing Planning

### Customer & Market Research
- Customer Interviews
- Reddit/Forum Research
- Review Mining (G2, App Store, Amazon)
- Social Listening & Sentiment
- JTBD Analysis
- ICP/Persona Research
- Market Intelligence
- Trend Detection
- Demand & Intent Research

### Competitive Intelligence
- Competitor Websites & Positioning
- SEO Competitor Analysis
- Ad Library Research
- Social & Content Competitor Intel
- Pricing Intelligence
- Traffic & Backlink Analysis
- Comparison/Alternative Pages

### SEO
- Technical SEO (crawlability, indexation, speed)
- On-Page SEO (titles, metas, headers, content)
- Keyword Research & Topical Authority
- Programmatic SEO
- Local & International SEO
- Link Building & Digital PR
- Schema & Structured Data
- Site Architecture & Internal Linking
- SERP Analysis

### AI Search (AEO/GEO)
- Answer Engine Optimization (AEO)
- Generative Engine Optimization (GEO)
- LLM Optimization (LLMO)
- Entity & Citation Optimization
- AI Search Analytics & Monitoring
- Multi-Surface Visibility (ChatGPT, Perplexity, Claude, Gemini)

### Paid Acquisition
- Meta Ads (Facebook/Instagram)
- Google Ads (Search/Display/YouTube/PMax)
- LinkedIn Ads
- X/Twitter Ads
- Reddit Ads
- TikTok Ads
- Pinterest Ads
- Amazon Ads
- Programmatic & Native
- Podcast/Newsletter Ads

### Ad Creative
- Hooks & Headlines
- UGC Creative
- Static/Video/Carousel Ads
- Advertorials
- Creative Research & Testing
- Fatigue Detection
- Ad Libraries Analysis

### Content & Editorial
- Content Strategy
- Blog Posts & Articles
- Newsletters
- Case Studies & Whitepapers
- Thought Leadership
- Content Repurposing
- Distribution Strategy

### Copywriting
- Landing Page Copy
- Conversion Copy
- Email Copy
- Ad Copy
- Video Scripts
- Microcopy & UX Writing

### Social Media
- LinkedIn (personal brand, company, ads)
- X/Twitter (threads, engagement, growth)
- Reddit (research, engagement, launches)
- TikTok (organic, shop, ads)
- YouTube (SEO, scripts, thumbnails)
- Instagram (Reels, Stories, feed)
- Discord & Telegram (community)

### Outbound & Sales
- Cold Email Sequences
- LinkedIn Outreach
- X/Twitter DM Outreach
- Multi-Channel Sequences
- Personalization & Research
- CRM & RevOps
- Sales Enablement

### Lifecycle & Email
- Onboarding Sequences
- Welcome Flows
- Nurture Campaigns
- Retention & Reactivation
- Transactional Email
- Newsletters
- Deliverability

### CRO & Experimentation
- Landing Page CRO
- Signup Flow Optimization
- Checkout Optimization
- Forms & Paywalls
- A/B & Multivariate Testing
- Experimentation Frameworks
- Pricing Page Optimization

### Analytics & Attribution
- GA4/GTM Implementation
- Conversion Tracking & Pixels
- Attribution Models
- MMM & Incrementality
- Funnel Analysis
- CAC/LTV/ROAS/MER Metrics
- Dashboard Design

### E-commerce/DTC
- Shopify Marketing
- PDP Optimization
- Email/SMS for Ecommerce
- Abandoned Cart Flows
- Subscriptions & Bundles
- Amazon Marketing
- TikTok Shop

### Automation & Agents
- Workflow Design (n8n/Zapier/Make)
- CRM Automation
- Lead Routing & Enrichment
- AI Marketing Agents
- MCP Server Integration

---

## KPI Tree

`
Revenue
├── New Revenue
│   ├── Leads × Conversion Rate × ACV
│   ├── CAC (by channel)
│   └── Payback Period
├── Expansion Revenue
│   ├── Upsell Rate
│   ├── Cross-sell Rate
│   └── Net Revenue Retention
└── Retained Revenue
    ├── Gross Retention
    ├── Churn Rate
    └── LTV

Traffic & Awareness
├── Organic (SEO + AI Search)
├── Paid (by platform)
├── Social (by platform)
├── Referral
├── Direct
└── Email

Engagement
├── Activation Rate
├── Feature Adoption
├── DAU/MAU
├── Session Duration
└── Pages per Session

Conversion
├── Visitor → Lead
├── Lead → MQL
├── MQL → SQL
├── SQL → Opportunity
├── Opportunity → Customer
└── Trial → Paid
`

## Persona Format

`yaml
persona:
  name: [Persona Name]
  role: [Job Title]
  company_size: [Range]
  industry: [Industry]
  seniority: [IC / Manager / Director / VP / C-Suite]
  goals:
    - [Goal 1]
    - [Goal 2]
  pain_points:
    - [Pain 1]
    - [Pain 2]
  buying_triggers:
    - [Trigger 1]
    - [Trigger 2]
  objections:
    - [Objection 1]
    - [Objection 2]
  channels:
    - [Where they hang out]
  content_preferences:
    - [What they read/watch]
  budget_authority: [Yes/No/Influencer]
  decision_process: [Solo / Committee / Procurement]
`

## Channel Families

| Family | Channels | Primary Metric |
|--------|----------|---------------|
| Search | SEO, Google Ads, AI Search | Traffic, Rankings, Citations |
| Social | LinkedIn, X, Reddit, TikTok, IG, YT | Engagement, Followers, Reach |
| Paid | Meta, Google, LinkedIn, X, TikTok Ads | ROAS, CAC, Conversions |
| Outbound | Cold Email, LinkedIn, X DMs | Reply Rate, Meetings Booked |
| Content | Blog, Newsletter, Podcast, YouTube | Subscribers, Traffic, Shares |
| Lifecycle | Email, In-app, SMS | Activation, Retention, LTV |
| Community | Discord, Slack, Reddit, Telegram | Members, Engagement, Advocacy |
| Partnerships | Affiliates, Influencers, Co-marketing | Revenue, Reach, Leads |