#!/usr/bin/env python3
"""
briefing-data.py — Fetch weather, markets, and news for daily briefings.

Usage:
    python3 briefing-data.py weather [--lat LAT] [--lon LON]
    python3 briefing-data.py markets [--symbols SYM1,SYM2]
    python3 briefing-data.py news [--topic TOPIC] [--limit N]

All sources have zero-config defaults. Optional API keys unlock richer data.

Environment variables:
    BRIEFING_LAT, BRIEFING_LON   — Location for weather
    BRIEFING_TZ                  — Timezone (default: America/Denver)
    GNEWS_API_KEY                — GNews API for structured news
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error
import urllib.parse
from datetime import datetime

WEATHER_CODE_MAP = {
    0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Foggy", 48: "Depositing rime fog",
    51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
    61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
    71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow",
    77: "Snow grains", 80: "Slight rain showers", 81: "Moderate rain showers",
    82: "Violent rain showers", 85: "Slight snow showers", 86: "Heavy snow showers",
    95: "Thunderstorm", 96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}

WIND_DIR = {0: "N", 45: "NE", 90: "E", 135: "SE", 180: "S", 225: "SW", 270: "W", 315: "NW"}

DEFAULT_EQUITIES = ["SPY", "QQQ", "DIA"]
DEFAULT_CRYPTO = ["BTC-USD", "ETH-USD"]


def c_to_f(c):
    return round(c * 9 / 5 + 32, 1) if c is not None else None


def kmh_to_mph(kmh):
    return round(kmh * 0.621371, 1) if kmh is not None else None


def nearest_wind_dir(deg):
    if deg is None:
        return "N/A"
    closest = min(WIND_DIR.keys(), key=lambda k: abs(k - deg))
    return WIND_DIR[closest]


def fetch_json(url, timeout=10):
    req = urllib.request.Request(url, headers={"User-Agent": "BriefingBot/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_weather(lat=None, lon=None):
    lat = lat or os.environ.get("BRIEFING_LAT", "43.58")
    lon = lon or os.environ.get("BRIEFING_LON", "-106.46")
    tz = os.environ.get("BRIEFING_TZ", "America/Denver")

    params = urllib.parse.urlencode({
        "latitude": lat, "longitude": lon,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m,wind_direction_10m",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max,sunrise,sunset",
        "timezone": tz, "forecast_days": "1",
    })
    url = f"https://api.open-meteo.com/v1/forecast?{params}"

    data = fetch_json(url)
    cur = data.get("current", {})
    daily = data.get("daily", {})

    code = cur.get("weather_code", 0)
    condition = WEATHER_CODE_MAP.get(code, "Unknown")

    result = {
        "current": {
            "temperature_f": c_to_f(cur.get("temperature_2m")),
            "feels_like_f": c_to_f(cur.get("apparent_temperature")),
            "condition": condition,
            "humidity_pct": cur.get("relative_humidity_2m"),
            "wind_speed_mph": kmh_to_mph(cur.get("wind_speed_10m")),
            "wind_direction": nearest_wind_dir(cur.get("wind_direction_10m")),
        },
        "today": {
            "temperature_max_f": c_to_f(daily.get("temperature_2m_max", [None])[0]),
            "temperature_min_f": c_to_f(daily.get("temperature_2m_min", [None])[0]),
            "precipitation_probability_max": daily.get("precipitation_probability_max", [None])[0],
            "sunrise": daily.get("sunrise", [None])[0],
            "sunset": daily.get("sunset", [None])[0],
        },
    }
    return result


def fetch_yahoo_chart(symbol):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?interval=1d&range=1d"
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (compatible; BriefingBot/1.0)"
    })
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    result = data.get("chart", {}).get("result", [{}])[0]
    meta = result.get("meta", {})
    price = meta.get("regularMarketPrice")
    prev = meta.get("chartPreviousClose") or meta.get("previousClose")
    change_pct = None
    if price and prev and prev != 0:
        change_pct = round((price - prev) / prev * 100, 2)
    return {"symbol": symbol, "price": round(price, 2) if price else None, "change_pct": change_pct}


def fetch_markets(equities=None, crypto=None):
    equities = equities or DEFAULT_EQUITIES
    crypto = crypto or DEFAULT_CRYPTO
    errors = []
    equities_data = []
    crypto_data = []

    for sym in equities:
        try:
            equities_data.append(fetch_yahoo_chart(sym))
        except Exception as e:
            errors.append(f"{sym}: {e}")

    for sym in crypto:
        try:
            raw = fetch_yahoo_chart(sym)
            crypto_data.append({
                "symbol": sym.replace("-USD", ""),
                "price_usd": raw.get("price"),
                "change_pct_24h": raw.get("change_pct"),
            })
        except Exception as e:
            errors.append(f"{sym}: {e}")

    return {"equities": equities_data, "crypto": crypto_data, "errors": errors}


def fetch_news_gnews(topic, limit=3):
    key = os.environ.get("GNEWS_API_KEY")
    if not key:
        return None
    params = urllib.parse.urlencode({"q": topic, "max": limit, "lang": "en", "token": key})
    url = f"https://gnews.io/api/v4/search?{params}"
    data = fetch_json(url)
    articles = []
    for a in data.get("articles", [])[:limit]:
        articles.append({"title": a.get("title"), "source": a.get("source", {}).get("name"), "url": a.get("url")})
    return {"articles": articles}


def main():
    parser = argparse.ArgumentParser(description="Fetch briefing data")
    parser.add_argument("command", choices=["weather", "markets", "news"])
    parser.add_argument("--lat", help="Latitude for weather")
    parser.add_argument("--lon", help="Longitude for weather")
    parser.add_argument("--topic", default=os.environ.get("BRIEFING_NEWS_TOPIC", "artificial intelligence"))
    parser.add_argument("--limit", type=int, default=3)
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON")
    args = parser.parse_args()

    try:
        if args.command == "weather":
            result = fetch_weather(args.lat, args.lon)
        elif args.command == "markets":
            result = fetch_markets()
        elif args.command == "news":
            result = fetch_news_gnews(args.topic, args.limit)
            if result is None:
                result = {"articles": [], "note": "GNEWS_API_KEY not set. Configure for news data."}
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)

    indent = 2 if args.pretty else None
    print(json.dumps(result, indent=indent, default=str))


if __name__ == "__main__":
    main()
