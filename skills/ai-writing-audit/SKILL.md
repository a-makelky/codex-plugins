---
name: ai-writing-audit
description: Audit content for AI writing patterns. Detects clichés, inflated phrases, weasel words, and structural red flags across 16+ categories. Input: draft content. Output: flagged issues + corrected text.
---

# AI Writing Audit Skill

Detect and flag AI writing patterns in content. Based on analysis of 100+ AI patterns found in generated text.

## Trigger

- Manual: `/ai-writing-audit` or "audit this for AI patterns"
- Automatic: Run on any draft before publishing

## Workflow

### Step 1: Pattern Scan

Scan for these categories of AI patterns:

#### AI-LEX (Instant AI Tells)
- delve, tapestry, unlock, empower, seamlessly
- robust, game-changer, synergy, leverage, holistic
- additionally, align with, emphasizing, enduring
- foster, garner, highlight, interplay, intricate
- showcase, spearhead, testament, transformative
- underscore, valuable, vibrant, enhance

#### INFLATED (Puffery)
- "stands as," "serves as," "is a testament to"
- "plays a vital role," "plays a crucial role"
- "highlighting the significance," "underscoring the importance"
- "demonstrates the power of," "exemplifies"

#### WEASEL (Vague Quantifiers)
- "some," "many," "various," "several"
- "experts argue," "observers note"
- "industry reports suggest"
- Any quantifier without a specific number

#### NOT-ONLY-BUT (False Balance)
- "Not only X, but Y"
- "It's not just about X, it's about Y"
- "However" pivots creating artificial balance

#### SUPERFICIAL-ING (Empty Modifiers)
- Present participle phrases: "ensuring," "reflecting," "highlighting," "underscoring"
- "contributing to broader," "demonstrating the importance"

#### PROMO (Marketing Fluff)
- "groundbreaking," "stunning," "world-class"
- "nestled in the heart of," "boasts a"
- "continues to captivate," "tourism/commercial tone"

#### DIRECT-ADDRESS (Didactic)
- "In this article, we will explore"
- "It's important to note"
- "worth remembering"
- "Let's dive in"

#### EM-OJI-MARKDOWN
- Emoji in running text
- Hashtags in body (LinkedIn)
- Excessive formatting (## headers in short posts)

### Step 2: Flag Issues

Output format:
```
## AUDIT

1. "[exact phrase]" [CATEGORY]
2. "[exact phrase]" [CATEGORY]
...

— END AUDIT: N issues found —
```

### Step 3: Provide Corrections

For each flagged issue, provide:
- The problematic phrase
- Why it's a problem
- Suggested replacement or deletion

### Step 4: Rewrite

Produce a corrected version that:
- Removes all flagged patterns
- Maintains the original meaning
- Improves clarity and directness

## Categories Reference

| Category | Description | Example |
|----------|-------------|---------|
| AI-LEX | AI cliché words | "delve," "tapestry," "unlock" |
| INFLATED | Overblown phrases | "stands as a testament to" |
| WEASEL | Vague without numbers | "many experts argue" |
| NOT-ONLY-BUT | False balance structure | "Not only X, but Y" |
| SUPERFICIAL-ING | Empty -ing phrases | "highlighting the importance" |
| PROMO | Marketing fluff | "groundbreaking," "world-class" |
| DIRECT-ADDRESS | Didactic asides | "It's important to note" |
| RULE-OF-3 | Forced parallelism | "Adjective, adjective, and adjective" |
| EM-DASH | Overused em-dashes | Multiple em-dash pairs per paragraph |
| CURLY-QUOTES | Smart quotes | " " instead of " " |
| MARKDOWN | Excessive formatting | ## headers in short posts |
| EMOJI | Emoji in text | 🚀 💡 ✨ |
| VAGUE-ATTR | Unnamed sources | "Experts argue" |
| KNOWLEDGE-CUTOFF | AI hedging | "as of my last update" |
| COLLAB | AI servant language | "Would you like me to..." |
| LETTER-FORMAT | Fake letter | "Dear X," "I hope this finds you" |
| PLACEHOLDER | Unfilled brackets | "[Enter Name]" |

## Example

**Input:**
```
In today's rapidly evolving landscape, organizations must leverage transformative AI tools to unlock their full potential. This is not only about technology, but about fostering a culture of innovation that empowers teams to seamlessly collaborate.

Many experts argue that the key to success lies in a holistic approach that underscores the importance of alignment across various stakeholders.
```

**Output:**
```
## AUDIT

1. "In today's rapidly evolving landscape" [AI-LEX]
2. "leverage" [AI-LEX]
3. "transformative" [AI-LEX]
4. "unlock their full potential" [AI-LEX]
5. "This is not only about technology, but about" [NOT-ONLY-BUT]
6. "fostering" [AI-LEX]
7. "empowers" [AI-LEX]
8. "seamlessly" [AI-LEX]
9. "Many experts argue" [VAGUE-ATTR] [WEASEL]
10. "the key to success" [AI-LEX]
11. "holistic" [AI-LEX]
12. "underscores the importance" [INFLATED]
13. "various" [WEASEL]

— END AUDIT: 13 issues found —

## CORRECTED TEXT

Organizations need AI tools that work. Success comes from getting teams to actually use them.

The fix is simple: pick one tool, train everyone on it, and measure whether it saves time.
```

## Quality Standards

1. **Exhaustive** — Catch all patterns, not just obvious ones
2. **Specific** — Quote exact phrases, not general areas
3. **Actionable** — Provide clear corrections
4. **Honest** — Flag everything, even if it means major rewrites

## Troubleshooting

### Too many false positives
- Focus on AI-LEX and INFLATED categories first
- Context matters: "key" as a noun is fine, "key to success" is AI

### Missing real issues
- Check for structural patterns (NOT-ONLY-BUT, RULE-OF-3)
- Look for em-dash overuse
- Count "I" vs "you" statements

### Corrections change meaning
- Prioritize removal over replacement
- When in doubt, delete the inflated phrase entirely
- Keep the core message, lose the puffery

## Related Skills

- `linkedin-hook-writer` — Generates hooks from audited content
- Voice guide template — Define your authentic writing voice
