---
name: briefing-data
description: Fetch structured data for daily briefings. Weather via Open-Meteo, markets via public APIs, news via web search. Zero-config defaults with optional API keys for richer data.
---

# Briefing Data Skill

Fetch structured data for daily briefings from free public APIs.

## Trigger

- Automatic: Called by `briefing-engine` skill
- Manual: `/briefing-data weather`, `/briefing-data markets`, `/briefing-data news`

## Data Sources

### Weather (Open-Meteo — free, no API key required)

**Endpoint:** `https://api.open-meteo.com/v1/forecast`

**Parameters:**
- `latitude`, `longitude` (set in config)
- `current=temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m,wind_direction_10m`
- `daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,sunrise,sunset`
- `timezone=auto`
- `forecast_days=1`

**Returns:**
```json
{
  "current": {
    "temperature_f": 72.5,
    "condition": "Partly cloudy",
    "humidity_pct": 45,
    "wind_speed_mph": 8.2,
    "wind_direction": "SW"
  },
  "today": {
    "temperature_max_f": 78.1,
    "temperature_min_f": 52.3,
    "precipitation_probability_max": 15,
    "sunrise": "06:42 AM",
    "sunset": "07:18 PM"
  }
}
```

### Markets (Yahoo Finance via public endpoints — free, no API key required)

**Equity proxies:**
- SPY (S&P 500), QQQ (Nasdaq 100), DIA (Dow Jones)
- Fetch via: `https://query1.finance.yahoo.com/v8/finance/chart/SPY?interval=1d&range=1d`

**Crypto:**
- BTC-USD, ETH-USD
- Fetch via: `https://query1.finance.yahoo.com/v8/finance/chart/BTC-USD?interval=1d&range=1d`

**Fallback:** Web search for "SPY price today" if Yahoo is unavailable.

**Returns:**
```json
{
  "equities": [
    {"symbol": "SPY", "price": 527.43, "change_pct": 0.82},
    {"symbol": "QQQ", "price": 452.10, "change_pct": 1.15}
  ],
  "crypto": [
    {"symbol": "BTC", "price_usd": 72450, "change_pct_24h": 2.3},
    {"symbol": "ETH", "price_usd": 3540, "change_pct_24h": -0.8}
  ],
  "macro": [
    {"label": "10Y Treasury", "value": "4.32%"},
    {"label": "VIX", "value": "14.2"}
  ]
}
```

### News (Web search — free, uses Codex's built-in search)

**Query:** `top AI news today` (or configurable topic)

**Returns top 3 stories:**
```json
{
  "articles": [
    {
      "title": "...",
      "source": "...",
      "url": "..."
    }
  ]
}
```

**Optional upgrade:** If `GNEWS_API_KEY` is set, use GNews API for structured results.

## Configuration

Set these environment variables (all optional — defaults provided):

```
# Location (required for weather)
BRIEFING_LAT=43.58       # Default: Casper, WY
BRIEFING_LON=-106.46

# Timezone
BRIEFING_TZ=America/Denver

# News topic (default: "artificial intelligence")
BRIEFING_NEWS_TOPIC=artificial intelligence

# Optional API keys for richer data
ALPHAVANTAGE_API_KEY=    # Fallback equity data
GNEWS_API_KEY=           # Structured news feed
COINGECKO_API_KEY=       # Extended crypto data
```

## Error Handling

Each data source fails independently:
- Weather fails → show "Weather unavailable" in briefing
- Markets fail → show "Market data unavailable" in briefing
- News fails → show "News unavailable" in briefing
- Partial failures are fine — show what's available

## Output Format

All data sources output JSON to stdout. The `briefing-engine` skill consumes this JSON.

## Related Skills

- `briefing-engine` — Assembles data into formatted briefing
