---
name: transcript-scraper
description: Scrape transcripts and captions from YouTube, Instagram, TikTok, and X. Returns full text with timestamps. Requires Supadata API key.
---

# Transcript Scraper Skill

Fetch transcripts and captions from social media platforms.

## Supported Platforms

| Platform | Content Type | API Endpoint |
|----------|-------------|--------------|
| YouTube | Transcripts (with timestamps) | `/v1/youtube/transcript` |
| Instagram | Post captions and metadata | `/v1/instagram/post` |
| TikTok | Video captions and metadata | `/v1/tiktok/video` |
| Twitter/X | Tweet text and threads | `/v1/twitter/tweet` |

## Prerequisites

**Required:** `SUPADATA_API_KEY` environment variable

**API docs:** https://supadata.ai/docs

## Trigger

- Manual: "scrape this transcript" + [URL]
- Automatic: Called by `transcript-to-content` pipeline

## Workflow

### Step 1: Detect Platform

Parse the URL to determine the platform:
- `youtube.com` or `youtu.be` → YouTube
- `instagram.com` → Instagram
- `tiktok.com` → TikTok
- `twitter.com` or `x.com` → X/Twitter

### Step 2: Fetch Transcript

**YouTube (primary use case):**

```bash
curl -s -H "x-api-key: $SUPADATA_API_KEY" \
  "https://api.supadata.ai/v1/youtube/transcript?url=VIDEO_URL&lang=en"
```

Response structure:
```json
{
  "lang": "en",
  "content": [
    {
      "lang": "en",
      "text": "Segment text here",
      "offset": 240,
      "duration": 6160
    }
  ]
}
```

**Critical:** Always include `lang=en` in YouTube requests. Without it, the API may return non-English subtitles when multiple community-translated tracks exist.

### Step 3: Extract Full Text

Combine all segments into clean text:

```bash
curl -s -H "x-api-key: $SUPADATA_API_KEY" \
  "https://api.supadata.ai/v1/youtube/transcript?url=VIDEO_URL&lang=en" | \
  jq -r '.content[].text' | tr '\n' ' '
```

### Step 4: Extract with Timestamps (Optional)

```bash
curl -s -H "x-api-key: $SUPADATA_API_KEY" \
  "https://api.supadata.ai/v1/youtube/transcript?url=VIDEO_URL&lang=en" | \
  jq -r '.content[] | "[\(.offset / 1000 | floor)s] \(.text)"'
```

## Output Format

```json
{
  "platform": "youtube",
  "url": "https://youtube.com/watch?v=...",
  "lang": "en",
  "full_text": "Complete transcript text...",
  "segments": [
    {"offset_sec": 0, "text": "..."},
    {"offset_sec": 6, "text": "..."}
  ],
  "metadata": {
    "title": "Video title",
    "channel": "Channel name",
    "duration_seconds": 1200
  }
}
```

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| Missing API key | `SUPADATA_API_KEY` not set | Set in environment |
| Invalid URL | Malformed URL | Verify URL format |
| No transcript | Video has no captions | Cannot proceed — no transcript available |
| Wrong language | Missing `lang=en` param | Add `lang=en` to YouTube requests |
| Rate limited | Too many requests | Wait and retry |

## Notes

- Auto-generated captions may have errors — use as starting point, not definitive source
- Very long videos (60+ min) produce large transcripts — consider processing in chunks
- Respect content rights — only scrape content you have permission to use
- Always attribute the original creator when using scraped content

## Related Skills

- `insight-extractor` — Extract key ideas from transcripts
- `transcript-to-content` — Full pipeline from URL to post
