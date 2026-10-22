# Busan Local Guide — Taiwan & Japan itinerary project

A public travel-guide prototype for **Taiwanese (Traditional Chinese)** and **Japanese** visitors to Busan.

## Site

- [Home](https://cute-00.github.io/busan-local-guide/)
- [🇹🇼 2天1夜 / 3天2夜（繁體中文）](https://cute-00.github.io/busan-local-guide/itineraries/zh.html)
- [🇯🇵 1泊2日 / 2泊3日（日本語）](https://cute-00.github.io/busan-local-guide/itineraries/ja.html)

The two localized pages contain **illustrative** day-by-day time tables with specific restaurants and links to location searches. Times are suggested slots, not guaranteed opening hours, reservations, or travel-time estimates.

## Implemented

- Responsive static travel content in Traditional Chinese and Japanese, with language links
- Separate 1-night-2-day and 2-night-3-day schedules, including food stops
- Google Maps search links for each stop
- GitHub Pages deployment via `.github/workflows/deploy.yml`, triggered by site edits
- Scheduled Monday 09:00 KST workflow `.github/workflows/weekly-draft.yml` using `scripts/create_draft.py`
- Weekly bilingual itinerary **editorial outlines only** saved to `drafts/` after a successful run; no automatic public posting

## Not yet implemented

- Fresh restaurant/transport feeds or automated verification of opening hours, prices, closures or bookings
- AI-written, fact-checked articles or automatic translation publishing
- Automatic Instagram / Pinterest posting
- Approved affiliate links (Klook, etc.), analytics, or proven revenue
- Original on-location photos and complete SEO / marketing operations

## How to check

1. Visit [Actions](https://github.com/cute-00/busan-local-guide/actions), then the **Deploy Busan Local Guide** workflow.
2. Inspect the site; if a new page is unavailable, check whether the latest deployment completed.
3. Before publishing new recommendations, check [Visit Busan](https://www.visitbusan.net/), [Blue Line Park](https://www.bluelinepark.com/) and [Gamcheon Culture Village](https://www.gamcheon.or.kr/), plus the restaurants directly.

Keep API keys, personal details and affiliate credentials out of public repository files.
