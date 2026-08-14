# Marketing OS — Platform-Change Resilience

Marketing platforms change constantly: algorithm shifts, API changes, feature/policy changes, new ad formats, deprecated capabilities, new AI search behavior. Skills must not silently go obsolete.

## Detection methodology

For each domain, watch these change surfaces:

| Surface | Signal | Detection |
|---|---|---|
| API | endpoint deprecation, version bumps, rate limits | pinned `API vX.Y` in skills → flag on drift |
| Features | new/removed ad formats, targeting options, tools | platform changelogs, skill mentions of features |
| Policy | ad policy, compliance, privacy (GDPR/CCPA) | policy pages, legal changelogs |
| Algorithm | ranking/feed changes, AI search behavior | vendor announcements, industry press |
| Pricing | cost models, bid floors | vendor pricing pages |

## Refresh triggers

A skill's platform facts are stale when:
1. The skill references a dated claim ("as of 2026", hardcoded year) and the date is >12 months old
2. A pinned API version is superseded
3. A feature it documents was removed or renamed
4. A channel it names was sunset

## Cadence

- **Weekly:** integrity watchdog (`scripts/check-integrity.py`) — YAML validity, dangling refs, stale markers. Silent when healthy.
- **Quarterly:** human/agent review of platform-specific skills against vendor changelogs, prioritized by 🔴 (spend/publish) surfaces first.

## Ownership

The skill's `category` maps to an owner agent in `agents/agent-layer.md`. That agent owns refresh for its domain. When a platform change lands, the owner updates the affected SKILL.md, bumps `version`, and notes the change in the skill's body.

## What we intentionally do NOT support

Kept out of the skill set by design (documented so it's a decision, not a gap):
- Live API credentials — the OS is runtime-agnostic; account auth belongs to the harness, not the skills
- Per-platform trivia that changes weekly (exact bid floors, CPM snapshots) — skills state these as heuristics with "verify before shipping" rather than pinning them
- Channels with no meaningful organic or paid surface left to document
