---
name: content-intake
description: Automatically feed high-value content into the Hopper from notes, transcripts, and other sources. Scans for new material, extracts key insights, creates Hopper files with content angles.
---

# Content Intake Skill

Automatically feed raw material into the Content Flywheel Hopper.

## Trigger

- Manual: `/content-intake` or "feed the hopper"
- Scheduled: Run before content-flywheel (e.g., 1 hour before)

## Problem

Content gets created daily but never makes it to the production pipeline. Notes sit in inboxes, transcripts get filed and forgotten. The flywheel has nothing to process.

## Solution

Scan content sources, extract key insights, create Hopper files with source links and potential content angles.

## Content Sources

Define your sources by editing the list below. These are the default categories — customize to match your workflow:

### Priority 1: Daily Learning Notes
- **Pattern:** `YYYY-MM-DD-daily-learning.md` or similar
- **Extract:** Key concepts, follow-ups, closing reflections
- **Angles:** "What I learned from [topic]" or "How to [key concept]"

### Priority 2: Meeting Notes
- **Pattern:** Notes from recent meetings, standups, or calls
- **Extract:** Decisions made, problems solved, unexpected insights
- **Angles:** "The thing nobody said in the meeting" or "[Tool] saved us [time]"

### Priority 3: Research & Reading
- **Pattern:** Saved articles, bookmarks, notes from talks/videos
- **Extract:** Contrarian takes, specific data points, frameworks
- **Angles:** "Everyone says X. Here's what I found." or "[Number] things I got wrong about [topic]"

### Priority 4: Conversations & DMs
- **Pattern:** Interesting threads, questions that came up more than once
- **Extract:** The recurring question, the surprising answer
- **Angles:** "[Question I keep getting] — here's the real answer"

## Workflow

### Step 1: Scan for New Content

Check for files created in the last 24 hours across your configured sources.

### Step 2: Extract Insights

For each file:
1. Parse the content (markdown, JSON, or plain text)
2. Extract: title, key concepts, follow-ups, source URL
3. Identify 2-3 potential content angles

### Step 3: Create Hopper File

Write to your Hopper directory:

```markdown
---
source: [source-type]
source_url: [URL or file path]
created: YYYY-MM-DD
angles:
  - "[Angle 1]"
  - "[Angle 2]"
---

# [Title]

**Source:** [Where this came from]
**Date:** [Date]

## Key Concepts

- [Concept 1]: [1-2 sentence summary]
- [Concept 2]: [1-2 sentence summary]
- [Concept 3]: [1-2 sentence summary]

## Potential Angles

1. **[Angle 1]:** [Why this angle works]
2. **[Angle 2]:** [Why this angle works]

## Source Quote

> "[Direct quote that captures the core insight]"

## Follow-ups

- [Follow-up action or related topic]
```

### Step 4: Notify

Send a summary:
- Number of files processed
- Angles identified
- Hopper status (X items ready for the flywheel)

## Configuration

Edit these defaults to match your setup:

```
HOPPER_DIR: ./content-flywheel/hopper/
SOURCES:
  - ./notes/daily-learning/
  - ./notes/meetings/
  - ./notes/research/
SKIP_KEYWORDS: ["processed", "archived", "draft"]
```

## Notes

- Run BEFORE content-flywheel
- Don't duplicate content already in Hopper
- Skip sources without actionable insights
- Prioritize sources with high engagement potential

## Related Skills

- `content-flywheel` — Processes Hopper items into posts
