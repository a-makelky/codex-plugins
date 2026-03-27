---
name: briefing-engine
description: Assemble a daily intelligence briefing from your calendar, weather, markets, and news. Configurable sections. Runs on schedule or on demand.
---

# Briefing Engine Skill

Assemble a daily intelligence briefing from multiple data sources.

## Trigger

- Manual: `/briefing` or "daily briefing" or "morning briefing"
- Scheduled: Daily at your preferred time (e.g., 8:00 AM local)

## Sections

All sections are optional. Enable or disable in config.

### 1. Today's Schedule

Pulls from your calendar. Shows today's events with times and locations.

**Data source:** Calendar API or CLI tool
**Config:** `BRIEFING_CALENDAR_ENABLED=true`
**Default:** enabled

### 2. Environment

Current weather conditions and today's forecast.

**Data source:** `briefing-data` skill (Open-Meteo)
**Config:** `BRIEFING_WEATHER_ENABLED=true`
**Default:** enabled

### 3. Market Summary

Equity indices, crypto, and macro indicators.

**Data source:** `briefing-data` skill (Yahoo Finance / web search)
**Config:** `BRIEFING_MARKETS_ENABLED=true`
**Default:** enabled

### 4. Top News

Top 3 stories from your configured topic.

**Data source:** `briefing-data` skill (web search / GNews)
**Config:** `BRIEFING_NEWS_ENABLED=true`, `BRIEFING_NEWS_TOPIC=artificial intelligence`
**Default:** enabled

### 5. Daily Focus

One concrete suggestion for what to focus on today. Rotates by day of week.

**Config:** Customize messages in config or replace with your own.
**Default:** enabled

### 6. Personal Notes

Short encouragement or reminder. Rotates daily.

**Config:** Customize messages in config or replace with your own.
**Default:** enabled

## Configuration

```bash
# Timezone
BRIEFING_TZ=America/Denver

# Location (for weather)
BRIEFING_LAT=43.58
BRIEFING_LON=-106.46

# Section toggles
BRIEFING_CALENDAR_ENABLED=true
BRIEFING_WEATHER_ENABLED=true
BRIEFING_MARKETS_ENABLED=true
BRIEFING_NEWS_ENABLED=true
BRIEFING_FOCUS_ENABLED=true
BRIEFING_NOTES_ENABLED=true

# News topic
BRIEFING_NEWS_TOPIC=artificial intelligence

# Calendar names (if using Google Calendar)
BRIEFING_CALENDARS="Primary,Work,Family"

# Output
BRIEFING_OUTPUT_DIR=./briefings/
```

## Workflow

### Step 1: Fetch Data

Run each enabled data source via the `briefing-data` skill:
- Calendar events for today
- Weather for configured location
- Market data (equities, crypto, macro)
- Top 3 news stories

### Step 2: Assemble Briefing

Format into structured output:

```
=== DAILY INTELLIGENCE BRIEFING ===
Date: March 26, 2026 (Thursday)

--- SCHEDULE ---
- 9:00 AM: Team standup
- 10:30 AM: 1:1 with Sarah
- 3:30 PM: Kids pickup

--- ENVIRONMENT ---
Current: 54°F, overcast, wind 12 mph
Today: high 69°F / low 48°F, precip 10%
Sunrise 6:48 AM / Sunset 7:22 PM

--- MARKETS ---
- SPY: $527.43 (+0.82%)
- QQQ: $452.10 (+1.15%)
- DIA: $398.21 (+0.45%)
Crypto:
- BTC: +2.3% @ $72,450
- ETH: -0.8% @ $3,540

--- NEWS ---
1. [Story title] (Source)
   [URL]
2. [Story title] (Source)
   [URL]
3. [Story title] (Source)
   [URL]

--- FOCUS ---
Thursday: use AI for synthesis work, not just retrieval. Convert raw inputs into a decision memo.

--- PERSONAL ---
Do the useful thing while it is still small.

Generated: 08:00:23 MDT
```

### Step 3: Save and Deliver

- Save to `BRIEFING_OUTPUT_DIR/YYYY-MM-DD-briefing.md`
- Deliver via configured channel (terminal, file, notification)

## Customization

### Custom Focus Messages

Replace the default day-of-week messages with your own in config:

```
BRIEFING_FOCUS_MONDAY="Your Monday message"
BRIEFING_FOCUS_TUESDAY="Your Tuesday message"
# etc.
```

### Custom Personal Notes

Replace the default rotating messages:

```
BRIEFING_NOTES_1="Your first message"
BRIEFING_NOTES_2="Your second message"
# etc.
```

### Custom News Topics

Change the news section to track any topic:

```
BRIEFING_NEWS_TOPIC=cryptocurrency
BRIEFING_NEWS_TOPIC=startups
BRIEFING_NEWS_TOPIC=cybersecurity
```

### Multiple Calendars

List all calendar names to aggregate:

```
BRIEFING_CALENDARS="Personal,Work,Family,Consulting"
```

## Error Handling

- Each section fails independently — show what's available
- If all data sources fail, output a minimal briefing with date and "data unavailable" for each section
- Log errors for debugging but never crash the briefing

## Quality Standards

1. **Complete** — All enabled sections present every day
2. **Fast** — Under 30 seconds total fetch time
3. **Resilient** — Partial failures don't block the briefing
4. **Readable** — Clean formatting, no raw JSON in output

## Related Skills

- `briefing-data` — Fetches weather, markets, and news
