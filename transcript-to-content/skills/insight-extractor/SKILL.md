---
name: insight-extractor
description: Extract key concepts, quotes, and content angles from transcripts. Turns raw transcript text into structured insights ready for content creation.
---

# Insight Extractor Skill

Extract key concepts, quotes, and content angles from transcripts.

## Trigger

- Manual: "extract insights from this transcript"
- Automatic: Called by `transcript-to-content` pipeline (Step 2)

## Input

Raw transcript text (from `transcript-scraper` skill) or pasted text.

## Workflow

### Step 1: Read Transcript

Load the full transcript. For long transcripts (60+ min videos), process in logical chunks (by topic shift or every 10 minutes).

### Step 2: Extract Key Concepts

Identify the 5-10 most important ideas:

For each concept:
- **Concept name:** Short label
- **Summary:** 1-2 sentence explanation
- **Evidence:** Direct quote or timestamp reference
- **Why it matters:** Why someone should care

### Step 3: Extract Best Quotes

Find 3-5 direct quotes worth keeping:
- Memorable statements
- Contrarian takes
- Specific data points or frameworks
- Actionable advice

Format:
```
> "[Exact quote]" — [timestamp or context]
```

### Step 4: Identify Content Angles

Generate 2-3 angles for turning this into content:

For each angle:
- **Hook idea:** One-line summary of the angle
- **Target audience:** Who would find this useful
- **Platform fit:** LinkedIn, X, blog, or video
- **Why it works:** Why this angle resonates

### Step 5: Identify Follow-ups

List related topics worth exploring:
- Deeper dives into specific concepts
- Contrarian takes to research
- Practical applications to test
- People or tools mentioned worth following up on

## Output Format

```markdown
---
source: [URL or filename]
platform: youtube
title: [Video/Content title]
creator: [Channel/Author name]
duration: [Length]
extracted: YYYY-MM-DD
---

# [Title]

**Source:** [URL]
**Creator:** [Name]
**Duration:** [Length]

## Key Concepts

### 1. [Concept Name]
[1-2 sentence summary]

> "[Supporting quote]" — [timestamp]

### 2. [Concept Name]
[1-2 sentence summary]

> "[Supporting quote]" — [timestamp]

[... continue for 5-10 concepts]

## Best Quotes

1. > "[Quote]" — [timestamp]
2. > "[Quote]" — [timestamp]
3. > "[Quote]" — [timestamp]

## Content Angles

1. **[Angle 1]:** [Why it works]
   - Platform: [LinkedIn/X/blog]
   - Audience: [Who]

2. **[Angle 2]:** [Why it works]
   - Platform: [LinkedIn/X/blog]
   - Audience: [Who]

3. **[Angle 3]:** [Why it works]
   - Platform: [LinkedIn/X/blog]
   - Audience: [Who]

## Follow-ups

- [ ] [Follow-up action 1]
- [ ] [Follow-up action 2]
- [ ] [Follow-up action 3]
```

## Quality Standards

1. **Accurate** — Quotes must be verbatim from transcript
2. **Specific** — Each concept has a concrete example or quote
3. **Actionable** — Angles must be publishable, not just interesting
4. **Complete** — Cover the main thesis of the content, not just surface-level takeaways

## Troubleshooting

### Too many concepts
- Focus on the 5 most impactful ideas
- Group related concepts together
- Ask: "If I could only share one thing, what would it be?"

### No good quotes
- Look for specific numbers or data points
- Find the clearest statement of the main thesis
- Paraphrase the core argument if no clean quote exists

### Angles feel generic
- Find the most surprising or contrarian point
- Focus on practical application, not theory
- Ask: "What would make someone stop scrolling for this?"

## Related Skills

- `transcript-scraper` — Fetches the transcript (upstream)
- `transcript-to-content` — Full pipeline orchestrator
