# Transcript to Content

Paste a URL, get publish-ready content.

## What's Inside

**3 skills, 1 pipeline.**

### Transcript Scraper
Fetches transcripts from YouTube, Instagram, TikTok, and X via Supadata API. Returns full text with timestamps. Handles auto-generated captions, multiple languages, and rate limits.

### Insight Extractor
Turns raw transcript text into structured insights: 5-10 key concepts, 3-5 best quotes, 2-3 content angles, and follow-up topics. Works for any transcript length.

### Transcript to Content (Orchestrator)
Ties it all together. Paste a URL → scrape transcript → extract insights → select best angle → draft post in your voice → audit for AI patterns → generate 10 hooks → deliver a complete content package.

## The Pipeline

```
URL → Scrape Transcript → Extract Insights → Select Angle → Draft in Voice → Audit + Hooks → Publish-ready Post
```

## Quick Start

1. Set `SUPADATA_API_KEY` (get one at https://supadata.ai)
2. Paste any URL: "Turn this into a post: https://youtube.com/watch?v=..."
3. Get a complete content package with draft, hooks, and source references

## Supported Platforms

| Platform | Content Type |
|----------|-------------|
| YouTube | Transcripts (with timestamps) |
| Instagram | Post captions and metadata |
| TikTok | Video captions and metadata |
| Twitter/X | Tweet text and threads |

## Use Cases

- **"Learn in public" creators** — Watch a video, turn it into a post
- **Podcasters** — Convert episode transcripts into LinkedIn threads
- **Researchers** — Extract key insights from talks and presentations
- **Consultants** — Turn client conversations into thought leadership
- **Anyone** who consumes content and wants to share what they learned

## Output

Every run produces a complete content package:
- Drafted post (with recommended hook)
- 3 alternative hook options
- Key concepts referenced
- Source quotes with timestamps
- Follow-up actions

## Origin

Built from a daily workflow that processes YouTube videos into LinkedIn posts. The scraper handles the `lang=en` edge case that trips up most transcript APIs. The insight extractor was refined over 6 months of daily use.

## Requirements

- `SUPADATA_API_KEY` — Free tier available at https://supadata.ai
- (Optional) Voice guide for voice-aligned drafting

## License

MIT
