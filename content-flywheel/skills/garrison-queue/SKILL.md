---
name: garrison-queue
description: Manage the posting queue. Move forged content to ready-to-post, track what's been published, and archive completed posts. Triggers: "queue status", "ready to post", "mark posted", "archive".
---

# Garrison Queue Skill

Manage the content posting queue: Forge → Garrison → Archives.

## Trigger Patterns

| User Says | Action |
|-----------|--------|
| "queue status" or "what's ready to post?" | Show counts across all stages |
| "move [topic] to queue" | Forge → Garrison |
| "mark [topic] posted" | Garrison → Archives |
| "list queue" | Show Garrison contents |
| "what should I post?" | Recommend from Garrison |

## Directory Structure

```
content-flywheel/
├── forge/           # Drafted + audited + hooked (review needed)
├── garrison/        # Ready to post (queue)
├── archives/        # Posted content (history)
```

## Commands

### Queue Status

Report:
- Count in Forge (pending review)
- Count in Garrison (ready to post)
- Count in Archives (posted this month)

### Move to Garrison

1. Find matching file in `forge/`
2. Add posting metadata to frontmatter:

```yaml
---
status: garrison
platform: linkedin
added_to_garrison: YYYY-MM-DD HH:MM
ready_to_post: true
---
```

3. Move to `garrison/`
4. Confirm

### Mark Posted

1. Find file in `garrison/`
2. Add posting metadata:

```yaml
---
status: posted
posted_date: YYYY-MM-DD HH:MM
posted_platform: linkedin
post_url: [optional]
---
```

3. Move to `archives/YYYY-MM/`
4. Confirm

### List Queue

Show Garrison contents with:
- Topic
- Platform
- Date added
- Ready status

### Recommend

Priority logic:
1. Garrison content first (ready to post)
2. Newest content first (freshest)
3. Provide the specific action to take

## Frontmatter Schema

### Forge
```yaml
---
created: YYYY-MM-DD HH:MM
source: [filename]
status: forged
platform: linkedin
---
```

### Garrison
```yaml
---
created: YYYY-MM-DD HH:MM
source: [filename]
status: garrison
platform: linkedin
added_to_garrison: YYYY-MM-DD HH:MM
ready_to_post: true
---
```

### Archives
```yaml
---
status: posted
posted_date: YYYY-MM-DD HH:MM
posted_platform: linkedin
post_url: [optional]
---
```

## Manual Posting Workflow

1. Run queue status to see what's ready
2. Review the file in Garrison
3. Copy final draft + selected hook
4. Post to platform
5. Mark posted to archive

## Related Skills

- `content-flywheel` — Produces forged content (upstream)
- `content-writer` — Writes in voice
- `ai-writing-audit` — Cleans AI patterns
- `linkedin-hook-writer` — Generates hooks
