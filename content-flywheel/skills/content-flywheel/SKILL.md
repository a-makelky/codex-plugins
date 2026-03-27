---
name: content-flywheel
description: Orchestrate the full content pipeline. Scans the Hopper, drafts in voice, audits for AI patterns, generates hooks, and delivers to the Forge. Trigger manually or on a schedule.
---

# Content Flywheel Skill

End-to-end content pipeline: Hopper → Forge → Garrison → Archives.

## Trigger

- Manual: `/content-flywheel` or "run the flywheel"
- Scheduled: Daily (recommended: 3:00 PM local time)

## Prerequisites

- Voice guide file exists (see `references/voice-guide-template.md`)
- Hopper directory exists with content to process

## Directory Structure

```
content-flywheel/
├── hopper/          # Raw notes, transcripts, ideas (input)
├── forge/           # Drafted + audited + hooked content (output)
├── garrison/        # Ready to post (queue)
├── archives/        # Posted content (history)
└── hopper/processed/  # Consumed inputs
```

## Pipeline

```
                    ┌─────────────┐
                    │   Hopper    │  Raw notes, transcripts, ideas
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  Intake     │  Extract insights, identify angles
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │   Writer    │  Draft in your voice
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │   Audit     │  Catch AI patterns (16+ categories)
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │   Hooks     │  Generate 10 pattern-breaking hooks
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │   Forge     │  Package as publish-ready file
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  Garrison   │  Queue for posting
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  Archives   │  Track what was posted
                    └─────────────┘
```

## Workflow

### Step 1: Scan the Hopper

Check the `hopper/` directory for markdown files.

- If empty: Report and exit
- If files exist: Process each in sequence

### Step 2: Draft Content

For each file:
1. Read the raw input
2. Apply `content-writer` skill using voice guide
3. Generate a voice-aligned draft

### Step 3: Audit for AI Patterns

Run `ai-writing-audit` on the draft:
- Flag all AI patterns
- Provide corrections
- Generate cleaned version

### Step 4: Generate Hooks

Run `linkedin-hook-writer` on the audited content:
- Generate 10 hooks using all 5 techniques
- Recommend top 3

### Step 5: Package and File

Create a forged content file in `forge/`:

```markdown
---
created: YYYY-MM-DD HH:MM
source: [original hopper filename]
status: forged
platform: linkedin
---

# Original Input

[Raw notes from Hopper]

---

# Draft

[Voice-aligned draft]

---

# Audit

[AI pattern flags and corrections]

---

# Audited Draft

[Cleaned version after corrections]

---

# Hook Options

[10 hooks from all 5 techniques]

---

# Top 3 Recommended Hooks

1. [Hook 1]
2. [Hook 2]
3. [Hook 3]
```

Filename format: `YYYY-MM-DD-Topic-Slug.md`

### Step 6: Archive Source

Move processed Hopper files to `hopper/processed/YYYY-MM-DD/`.

### Step 7: Notify

Report:
- Items forged
- Items remaining in Hopper
- Items in Garrison ready to post

## Error Handling

- **Missing voice guide:** Log error, skip drafting, notify
- **Skill failure:** Log error, continue to next file, include partial results
- **Empty Hopper:** Report and exit cleanly

## Quality Standards

1. **Voice accuracy** — Sounds like the author, not AI
2. **Zero AI patterns** — Audit catches all tells
3. **Actionable hooks** — Pattern-breaking, under 55 chars
4. **Complete package** — Everything needed to post in one file

## Related Skills

- `content-intake` — Feed the Hopper
- `content-writer` — Step 2
- `ai-writing-audit` — Step 3
- `linkedin-hook-writer` — Step 4
- `garrison-queue` — Manage posting queue
