---
name: content-writer
description: Write content in your personal brand voice using a voice guide. Input: raw notes, transcript, or topic. Output: voice-aligned draft ready for audit.
---

# Content Writer Skill

Write content in your authentic voice using your voice guide.

## Prerequisites

A voice guide file must exist. This is a markdown file that defines your writing voice — tone, word choices, sentence patterns, platform rules, and anti-patterns.

**Default location:** `./voice-guide.md`

If no voice guide exists, the writer will produce clean, direct prose but won't be calibrated to your specific voice. Create a voice guide using the template in `references/voice-guide-template.md`.

## Trigger

- Manual: `/content-writer` or "write this in my voice"
- Called by: Flywheel system (Step 2 of the pipeline)

## Workflow

### Step 1: Read Voice Guide

Load your voice guide to understand:
- Core voice traits and tone
- Who you are and what makes your perspective unique
- Words and phrases to avoid
- Sentence patterns and rhythm
- Platform-specific rules

### Step 2: Understand the Input

Accept any of:
- Raw notes (bullet points, fragments)
- Transcript (meeting, video, audio)
- Rough draft needing voice alignment
- Topic + key points

### Step 3: Extract Core Message

Identify:
1. **The one thing** — What's the single most important point?
2. **The pain** — What problem does this solve?
3. **The fix** — What's the tactical solution?
4. **The proof** — What evidence supports this?

### Step 4: Write in Voice

**DO:**
- Start with BLUF (Bottom Line Up Front)
- Use short declarative sentences
- Be specific and tactical — names, tools, dollar amounts, time saved
- Use second person ("you") for advice
- Use contractions (don't, can't, it's)
- Write like you'd speak to a colleague
- Show your work (test things, share results)
- Be documentary, not performance

**DON'T:**
- Use any words from your voice guide's blacklist
- Write "Not only X, but Y" patterns
- Use em-dashes for punchy parallelism
- Add emoji or hashtags (unless platform-specific rules allow)
- Hedge ("somewhat," "fairly," "quite")
- Use inflated phrases ("plays a vital role," "stands as a testament to")
- Write SaaS marketing copy
- Sound like a LinkedIn influencer
- Be pretentious or performative

### Step 5: Platform Formatting

**LinkedIn:**
- Reader-focused (more "you" than "I")
- Hook: 2 lines, ~55 chars each, pattern-breaking
- Body: 3-5 short paragraphs
- No hashtags in body

**X/Twitter:**
- Single idea per tweet
- Even shorter, punchier
- Threads for complex topics (5-8 tweets max)

**Blog / Long-form:**
- Most polished version
- Full story arc with evidence
- Sections with clear purpose

### Step 6: Output Format

```markdown
---
platform: linkedin | x | blog
created: YYYY-MM-DD
source: [original input reference]
---

# Body

[Content in voice — no hook yet, that comes from linkedin-hook-writer]

---

## Voice Check
- [ ] No blacklisted words
- [ ] No inflated phrases
- [ ] More "you" than "I"
- [ ] Specific, not vague
- [ ] Would I say this out loud?
```

## Quality Standards

1. **Voice accuracy** — Sounds like the author, not AI
2. **Specific** — Concrete details, not vague claims
3. **Reader-focused** — About the audience, not achievements
4. **Tactical** — Actionable advice

## Troubleshooting

### Output sounds like AI
- Re-read the voice guide blacklist
- Check for influencer patterns ("game changer," "5 reasons," "today")
- Count "you" vs "I" statements
- Ask: "Would I say this out loud?"

### Too vague/generic
- Add specific numbers
- Name specific tools/features
- Include concrete examples

### Wrong platform tone
- LinkedIn: more reader-focused, longer form
- X: shorter, punchier, single idea

## Related Skills

- `ai-writing-audit` — Audit output for AI patterns (next step)
- `linkedin-hook-writer` — Generate hooks after audit
- `content-flywheel` — Orchestrates the full pipeline
