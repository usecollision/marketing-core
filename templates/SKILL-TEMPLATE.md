---
name: [skill-name]
category: [domain]
description: [One-line description of what this skill does]
triggers:
  - "[trigger phrase 1]"
  - "[trigger phrase 2]"
inputs:
  - product_context
  - [other required inputs]
outputs:
  - [primary output]
  - [secondary outputs]
related_skills:
  - [skill-1]
  - [skill-2]
required_context:
  - .context/product-marketing.md
  - .context/brand-profile.json
allowed_tools:
  - [mcp:tool-name or none]
version: 1.0.0
---

## When to Use

[Precise activation conditions - when should an agent invoke this skill? Include trigger phrases, synonyms, and scenarios.]

## Read Context First

Before executing, read:
1. .context/product-marketing.md - Product, ICP, positioning, value props
2. .context/brand-profile.json - Brand voice, tone, guidelines
3. .context/project-context.md - Current goals, constraints, timeline

## Workflow

### Step 1: [Phase Name]
[Instructions for this phase]

**Gate:** [Success criteria before moving to Step 2]

### Step 2: [Phase Name]
[Instructions for this phase]

**Gate:** [Success criteria before moving to Step 3]

### Step 3: [Phase Name]
[Instructions for this phase]

**Gate:** [Success criteria before completion]

## Frameworks & References

- See eferences/frameworks.md for [relevant frameworks]
- See eferences/examples.md for [sample inputs/outputs]
- See eferences/checklist.md for [QA checklist]

## Evaluation & QA

### Scoring Rubric
| Criteria | Score 1 (Poor) | Score 3 (Good) | Score 5 (Excellent) |
|----------|---------------|----------------|---------------------|
| [Criterion 1] | [description] | [description] | [description] |
| [Criterion 2] | [description] | [description] | [description] |
| [Criterion 3] | [description] | [description] | [description] |

### Common Failure Modes
- [Failure mode 1 and how to avoid]
- [Failure mode 2 and how to avoid]

## Tool Calls

[Example MCP or API interactions if relevant, otherwise remove this section]