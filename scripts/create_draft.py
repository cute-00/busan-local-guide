#!/usr/bin/env python3
"""Curated travel itinerary *review drafts* for Taiwan & Japan readers.

Runs weekly via GitHub Actions. No scraping, paid APIs or automatic publishing.
The draft is not fact-checked against live venue hours or ticket availability.
"""
from datetime import datetime, timedelta, timezone
from pathlib import Path

KST = timezone(timedelta(hours=9))
today = datetime.now(KST).date()

subjects = [
    {
        "slug": "2day-nampo-haeundae",
        "duration": "1 night / 2 days",
        "zh_title": "釜山2天1夜：南浦洞市場＋海雲臺海岸",
        "ja_title": "釜山1泊2日：南浦洞の市場＋海雲台の海",
        "areas": "Day 1: Gamcheon → 1969 Buwondong Kalguksu → Jagalchi/BIFF → ChoPilsal Nampo; Day 2: Haeundae → Blueline Park → Doheenae Cheongsapo"
    },
    {
        "slug": "3day-market-sea-village",
        "duration": "2 nights / 3 days",
        "zh_title": "釜山3天2夜：市場、海景、文化村",
        "ja_title": "釜山2泊3日：市場・海・文化村",
        "areas": "Day 1: Nampo, Jagalchi, ChoPilsal BBQ; Day 2: Haeundae, Blueline, Doheenae, Geumsubokguk, Gwangalli; Day 3: Gamcheon, Kalguksu, optional Huinnyeoul"
    },
    {
        "slug": "seafood-busan-coast",
        "duration": "1 night / 2 days",
        "zh_title": "釜山海景美食2天1夜：青沙浦與海雲臺",
        "ja_title": "釜山の海と海鮮を楽しむ1泊2日",
        "areas": "Day 1: Haeundae and Mipo; Day 2: Blueline/Cheongsapo and seafood lunch; choose Nampo only when departure transport allows"
    },
    {
        "slug": "slow-pace-busan",
        "duration": "2 nights / 3 days",
        "zh_title": "慢遊釜山3天2夜：少換車的在地路線",
        "ja_title": "ゆったり釜山2泊3日：移動を減らす旅",
        "areas": "Day 1: Gamcheon + Nampo; Day 2: Haeundae + Cheongsapo + meal; Day 3: optional Yeongdo or leisure, then departure"
    }
]
week = today.isocalendar().week
subject = subjects[(week - 1) % len(subjects)]
base = Path(__file__).resolve().parents[1]
out = base / "drafts" / (today.isoformat() + "-" + subject["slug"] + ".md")
out.parent.mkdir(parents=True, exist_ok=True)
if out.exists():
    print("Draft already exists:", out.name)
    raise SystemExit(0)

draft = """---
status: NEEDS_HUMAN_REVIEW
languages: [zh-Hant, ja]
duration: {duration}
date: {date}
---

# Weekly Taiwan + Japan Busan itinerary brief
## Taiwan / 繁體中文
**{zh_title}**

- Write a factual, original itinerary introduction in Traditional Chinese.
- Provide a day-by-day schedule with time slots, Korean attraction names and map links.
- Explain the logic of the route, local food choices, and transit considerations.

## Japan / 日本語
**{ja_title}**

- 日本人旅行者向けに、自然な日本語で観光スケジュールを執筆してください。
- 各日の時刻、立ち寄る飲食店の韓国語名称、地図リンクを必ず付けてください。
- 移動負担・食事時間・帰国便までの余裕を考慮してください。

## Suggested locations (editorial outline only)
{areas}

## Human checks required before publishing
- [ ] Confirm each restaurant still operates and verify day-specific opening hours
- [ ] Confirm each venue's opening details and local transport connections
- [ ] Check coastal train/Sky Capsule inventory and ticket routes; do not invent reservations
- [ ] Verify suitable walking times against a real route planner
- [ ] Review Taiwan Traditional Chinese and Japanese translations
- [ ] Add original or appropriately licensed photos and clear credits
- [ ] Disclose affiliate commissions only if an approved affiliate account exists
- [ ] Obtain human editor approval and manually add content to published pages

## Official reference sites
- Busan City Tourism: https://www.visitbusan.net/
- Haeundae Blueline Park: https://www.bluelinepark.com/
- Gamcheon Culture Village: https://www.gamcheon.or.kr/

This file is an editorial brief, NOT a published article or independently verified restaurant schedule.
""".format(duration=subject["duration"], date=today.isoformat(), zh_title=subject["zh_title"], ja_title=subject["ja_title"], areas=subject["areas"])

out.write_text(draft, encoding="utf-8")
print("Created review draft:", out.relative_to(base))
