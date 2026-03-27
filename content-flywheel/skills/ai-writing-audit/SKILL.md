---
name: ai-writing-audit
description: Audit content for AI writing patterns. Part of the Content Flywheel pipeline. Detects clichés, inflated phrases, weasel words, and structural red flags across 16+ categories.
---

# AI Writing Audit Skill

Detect and flag AI writing patterns in content.

## Trigger

- Manual: `/ai-writing-audit` or "audit this for AI patterns"
- Automatic: Step 3 of the Content Flywheel pipeline

## Workflow

### Step 1: Pattern Scan

Scan for these categories:

| Category | What to catch | Examples |
|----------|---------------|---------|
| AI-LEX | AI cliché words | delve, tapestry, unlock, empower, seamlessly, robust, game-changer, synergy, leverage, holistic, additionally, foster, garner, showcase, spearhead, transformative, underscore, vibrant, enhance |
| INFLATED | Overblown phrases | "stands as a testament to," "plays a vital role," "demonstrates the power of" |
| WEASEL | Vague without numbers | "some," "many," "various," "experts argue," "industry reports suggest" |
| NOT-ONLY-BUT | False balance | "Not only X, but Y," "It's not just about X, it's about Y" |
| SUPERFICIAL-ING | Empty -ing phrases | "highlighting the importance," "contributing to broader" |
| PROMO | Marketing fluff | "groundbreaking," "world-class," "stunning" |
| DIRECT-ADDRESS | Didactic asides | "In this article, we will explore," "Let's dive in" |
| RULE-OF-3 | Forced parallelism | "Adjective, adjective, and adjective" |
| EM-DASH | Overused em-dashes | Multiple em-dash pairs per paragraph |
| EMOJI | Emoji in text | 🚀 💡 ✨ in running prose |
| MARKDOWN | Excessive formatting | ## headers in short posts |
| VAGUE-ATTR | Unnamed sources | "Experts argue," "Observers note" |
| KNOWLEDGE-CUTOFF | AI hedging | "as of my last update" |
| COLLAB | AI servant language | "Would you like me to..." |
| LETTER-FORMAT | Fake letter | "Dear X," "I hope this finds you" |
| PLACEHOLDER | Unfilled brackets | "[Enter Name]" |

### Step 2: Flag Issues

```
## AUDIT

1. "[exact phrase]" [CATEGORY]
2. "[exact phrase]" [CATEGORY]
...

— END AUDIT: N issues found —
```

### Step 3: Provide Corrections

For each flagged issue:
- The problematic phrase
- Why it's a problem
- Suggested replacement or deletion

### Step 4: Rewrite

Produce a corrected version:
- Removes all flagged patterns
- Maintains original meaning
- Improves clarity and directness

## Quality Standards

1. **Exhaustive** — Catch all patterns
2. **Specific** — Quote exact phrases
3. **Actionable** — Provide clear corrections
4. **Honest** — Flag everything, even if it means major rewrites

## Related Skills

- `content-writer` — Produces the draft to audit
- `linkedin-hook-writer` — Generates hooks from audited content
- `content-flywheel` — Orchestrates the pipeline
