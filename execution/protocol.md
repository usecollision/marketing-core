# Marketing OS — Execution Protocol

How a strategist skill's output becomes a real tool call. This is the binding
between the `allowed_tools` declarations and the live runtime.

## The pipeline

```
1. STRATEGIST RUNS
   A strategist skill (positioning, media-planning, seo-audit, ...) executes
   against context and produces its declared `outputs` — a structured plan,
   not a mutation.

2. EXECUTION BRIEF
   The skill's `outputs` are extracted into a brief. Each output maps to zero
   or more operator tools via execution/tool-registry.yaml.

3. GATE CHECK
   Every tool in the brief is classified:
     🔴 gated   -> STOP, show exact payload, wait for human approval
     🟡 scoped  -> read allowed; any write degrades to 🔴
     🟢 open    -> run
   The gate is enforced by the RUNTIME, not by the skill doc. A skill saying
   "mcp:meta-ads" does not grant write access — the registry's gate does.

4. OPERATOR CALL
   The mapped MCP tool executes (or is queued behind approval). Result feeds
   back into the next skill in the chain.
```

## The hard rules

1. **Read and draft are free.** Any skill that only reads (search, scrape,
   audit, analyze, plan) runs ungated.
2. **Spend, publish, send = 🔴.** Anything that spends money, publishes content,
   or messages a human stops and shows the exact artifact before running.
   This is non-negotiable and matches the agent's own hard rule.
3. **No write by default.** `scoped` tools have writes stripped unless the user
   explicitly widens the gate for a session.
4. **Degrade, never escalate.** A `scoped` tool asked to write degrades to
   🔴 approval; it never silently auto-approves.

## Example: "spend ₹4L on Google Search"

```
media-planning (strategist, 🟢) runs
  -> outputs: platform_selection=[google-search], budget_allocation={google: 400000}
  -> brief maps budget_allocation -> mcp:ads-platforms (markifact-mcp)
  -> gate check: mcp:ads-platforms = 🔴 gated
  -> STOP: "Proposed Google Search campaign: ₹4L budget, <exact structure>.
            Approve to create?" (shows payload)
  -> user approves -> markifact-mcp campaign-create executes
```

## Example: "why is my funnel leaking at signup?"

```
funnel-analysis (🟢) runs against GA4
  -> outputs: dropoff_report
  -> brief maps -> mcp:analytics (ga4-mcp, 🟡 scoped read)
  -> gate check: read = allowed, no approval
  -> GA4 query executes, report returns
  -> next skill in chain: signup-flow (🟢) proposes fixes, but any CRO change
     is a 🔴 write -> pauses for approval
```

## What's live today

Only the 🟢 open tools are wired (`web-search`, `web-scraper`). Every 🟡 and 🔴
tool is declared and mapped but blocked on credentials — see
execution/tool-registry.yaml for the exact status of each. Wiring a new tool is
a config change (`hermes mcp add ...` or `hermes config set mcp_servers...`),
followed by a fresh session to pick it up.

## Owning agent

Each gate is enforced by the specialist agent named in agents/agent-layer.md.
The director agent routes the strategist output; the specialist agent performs
the gated tool call. No skill executes a 🔴 tool directly — only through its
specialist agent, which is what makes the approval gate enforceable.
