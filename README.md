# marketing-core

The kernel of the UseCollision Marketing OS. Shared context, ontology, routing conventions, dependency rules, and universal frameworks that all domain repos depend on.

## Architecture

- context/ - Brand/product context templates
- frameworks/ - Universal marketing frameworks (AARRR, JTBD, etc.)
- ontology/ - Marketing taxonomy and capability definitions
- capability-catalog.md - The canonical capability universe (live vs planned, OSS reuse targets)
- oss-landscape.md - OSS discovery research (24 domains, ~190 repos)
- agents/agent-layer.md - Director/specialist/critic agent orchestration map
- execution/mcp-map.md - MCP server + tool wiring with capability gates
- resilience.md - Platform-change monitoring methodology
- scripts/check-integrity.py - Weekly integrity watchdog (silent when healthy)
- routing/ - Router skills and agent instructions (see AGENTS.md)
- templates/ - SKILL.md template and folder structure spec
- dependency-graph/ - Cross-repo dependency definitions

## How Domain Repos Use This

Every domain repo references marketing-core for:
1. Shared context - Skills read product-marketing.md, brand-profile.json, project-context.md before executing
2. Ontology - Consistent terminology, KPI trees, channel families, persona formats
3. Frameworks - Universal models (AARRR, JTBD, segmentation, funnels)
4. Routing - How agents discover and chain skills across repos
5. Dependency rules - Which skills depend on which, execution order

## Upstream Sources

This OS selectively imports and normalizes skills from:
- coreyhaines31/marketingskills
- indranilbanerjee/digital-marketing-pro
- kostja94/marketing-skills
- OpenClaudia/openclaudia-skills
- hyperfx-ai/marketing-skills
- BrianRWagner/ai-marketing-claude-code-skills
- nexscope-ai/eCommerce-Skills
- sales-skills/sales
- Shopify/agent-skills

## License

MIT