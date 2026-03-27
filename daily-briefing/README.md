# Daily Briefing Engine

Start every day with a structured intelligence packet.

## What's Inside

**2 skills + 1 data script.**

### Briefing Data
Fetches weather (Open-Meteo, free), markets (Yahoo Finance, free), and news (GNews, free tier). Each source fails independently — partial data is fine. Zero-config defaults with optional API keys for richer data.

### Briefing Engine
Assembles the data into a formatted briefing with 6 configurable sections: schedule, weather, markets, news, daily focus, and personal notes. Runs on a cron schedule or on demand.

### briefing-data.py
Standalone Python script that fetches data as JSON. Works without any API keys. `python3 briefing-data.py weather`, `python3 briefing-data.py markets`, `python3 briefing-data.py news --topic "cybersecurity"`.

## Quick Start

1. Set your location (optional — defaults to Casper, WY):
   ```
   BRIEFING_LAT=43.58
   BRIEFING_LON=-106.46
   BRIEFING_TZ=America/Denver
   ```

2. Set your news topic (optional — defaults to "artificial intelligence"):
   ```
   BRIEFING_NEWS_TOPIC=startups
   ```

3. Run: `/briefing` or "daily briefing"

4. (Optional) Add `GNEWS_API_KEY` for structured news results

## Sections

All sections are toggleable:

| Section | Default | Data Source |
|---------|---------|-------------|
| Schedule | On | Calendar API |
| Weather | On | Open-Meteo (free) |
| Markets | On | Yahoo Finance (free) |
| News | On | GNews / web search |
| Daily Focus | On | Rotating messages |
| Personal Notes | On | Rotating messages |

## Output

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

--- MARKETS ---
- SPY: $527.43 (+0.82%)
- QQQ: $452.10 (+1.15%)
Crypto:
- BTC: +2.3% @ $72,450

--- NEWS ---
1. [Story title] (Source)
2. [Story title] (Source)
3. [Story title] (Source)

--- FOCUS ---
Thursday: convert raw inputs into a decision memo.

--- PERSONAL ---
Do the useful thing while it is still small.

Generated: 08:00:23 MDT
```

## Customization

- Toggle sections with `BRIEFING_*_ENABLED=true/false`
- Custom news topics with `BRIEFING_NEWS_TOPIC`
- Custom focus messages with `BRIEFING_FOCUS_MONDAY`, etc.
- Custom personal notes with `BRIEFING_NOTES_1`, `BRIEFING_NOTES_2`, etc.
- Multiple calendars with `BRIEFING_CALENDARS="Personal,Work,Family"`

## Origin

Built from a production morning briefing that runs daily at 8 AM. The data script uses free APIs with no required keys — anyone can drop it in and run it.

## License

MIT
