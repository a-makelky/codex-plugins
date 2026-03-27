---
name: transcript-to-content
description: Full pipeline: paste a URL, get publish-ready content. Scrapes transcript, extracts insights, drafts post in your voice. Works for YouTube, Instagram, TikTok, and X.
---

# Transcript to Content Skill

End-to-end pipeline: URL → Transcript → Insights → Draft Post.

## Trigger

- Manual: "Turn this into a post: [URL]" or "Make content from this: [URL]"
- Quick: Just paste a YouTube, Instagram, TikTok, or X URL

## Prerequisites

- `SUPADATA_API_KEY` environment variable (for transcript scraping)
- Voice guide file (optional — see `references/voice-guide-template.md` from the Content Flywheel plugin)

## Pipeline

```
        ┌──────────────────┐
        │  Paste URL       │
        └────────┬─────────┘
                 │
        ┌────────▼─────────┐
        │  Detect Platform │
        │  (YT/IG/TT/X)    │
        └────────┬─────────┘
                 │
        ┌────────▼─────────┐
        │  Scrape Transcript│
        └────────┬─────────┘
                 │
        ┌────────▼─────────┐
        │  Extract Insights│
        │  (concepts,      │
        │   quotes, angles)│
        └────────┬─────────┘
                 │
        ┌────────▼─────────┐
        │  Select Angle    │
        └────────┬─────────┘
                 │
        ┌────────▼─────────┐
        │  Draft in Voice  │
        └────────┬─────────┘
                 │
        ┌────────▼─────────┐
        │  Audit + Hooks   │
        └────────┬─────────┘
                 │
        ┌────────▼─────────┐
        │  Deliver Post    │
        └──────────────────┘
```

## Workflow

### Step 1: Scrape Transcript

Use the `transcript-scraper` skill:
- Detect platform from URL
- Fetch full transcript with timestamps
- Handle errors (no transcript, wrong language, rate limits)

### Step 2: Extract Insights

Use the `insight-extractor` skill:
- Identify 5-10 key concepts
- Pull 3-5 best quotes
- Generate 2-3 content angles
- List follow-up topics

### Step 3: Select Best Angle

From the extracted angles, pick the strongest one based on:
- **Surprise factor** — Contrarian or unexpected
- **Specificity** — Has concrete details, numbers, or examples
- **Audience fit** — Solves a real problem for the target reader
- **Authenticity** — Matches the author's voice and expertise

If a voice guide exists, check that the angle aligns with the author's perspective and expertise.

### Step 4: Draft Content

Write the post using the selected angle:

**Structure:**
1. **Hook** (2 lines, ~55 chars each) — pattern-breaking opener
2. **Body** (3-5 paragraphs) — specific, actionable, reader-focused
3. **Close** — open-ended, no forced CTA

**Voice rules (if voice guide available):**
- Short declarative sentences
- Specific over vague (names, numbers, tools, time saved)
- "You" over "I"
- No AI clichés, no inflated phrases, no em-dash parallelism
- Documentary, not performance

### Step 5: Audit and Generate Hooks

Run AI pattern detection on the draft:
- Flag any AI writing patterns
- Provide corrections
- Generate 10 hook options using 5 techniques (contradiction, specific number, direct accusation, stolen thought, absurd reframe)
- Recommend top 3 hooks

### Step 6: Deliver

Output a complete content package:

```markdown
---
source: [URL]
platform: [youtube/instagram/tiktok/x]
title: [Original content title]
creator: [Channel/Author]
angle: [Selected angle]
created: YYYY-MM-DD
---

## Selected Angle

[One-line description of the angle chosen]

## Draft Post

[Full post text with recommended hook at top]

## Hook Options (Top 3)

1. [Hook 1] — [Technique used]
2. [Hook 2] — [Technique used]
3. [Hook 3] — [Technique used]

## Key Concepts Used

- [Concept 1]: [How it appears in the post]
- [Concept 2]: [How it appears in the post]

## Source Quotes Referenced

> "[Quote 1]" — [timestamp]
> "[Quote 2]" — [timestamp]

## Follow-ups

- [ ] [Action item 1]
- [ ] [Action item 2]
```

## Platform-Specific Output

### LinkedIn
- Hook: 2 lines, ~55 chars each
- Body: 3-5 short paragraphs
- No hashtags, no emoji

### X / Twitter
- Single idea per tweet
- Thread format for complex topics (5-8 tweets max)
- Shorter, punchier

### Blog / Long-form
- Full article format
- Sections with clear purpose
- More evidence and story arc

## Quick Commands

| You Say | What Happens |
|---------|-------------|
| "Turn this into a post: [URL]" | Full pipeline → draft post |
| "Scrape this: [URL]" | Transcript only |
| "Extract insights: [URL]" | Transcript + insights, no draft |
| "What are the angles here: [URL]" | Transcript + angles only |

## Error Handling

- **No transcript available:** Report and suggest alternatives (other videos, manual notes)
- **Transcript in wrong language:** Re-fetch with `lang=en` parameter
- **Very long content:** Process in chunks, summarize sections
- **No good angles found:** Report honestly — not every piece of content makes a good post

## Quality Standards

1. **Accurate** — Claims backed by transcript quotes
2. **Original** — Adds the author's perspective, doesn't just summarize
3. **Reader-focused** — About the audience, not the source creator
4. **Voice-aligned** — Sounds like the author, not AI
5. **Complete** — Ready to post with minimal editing

## Related Skills

- `transcript-scraper` — Fetches transcripts (Step 1)
- `insight-extractor` — Extracts key ideas (Step 2)
