#!/usr/bin/env python3
"""Create a weekly editorial review draft for Busan Local Guide.

No API keys or unverified claims are required. These are review templates,
NOT verified visitor guidance and NOT ready for automatic publication.
"""
from __future__ import annotations
from datetime import datetime, timezone, timedelta
from pathlib import Path
import sys

KST = timezone(timedelta(hours=9))
date = datetime.now(KST).date()
topics = [
    {
        "slug": "gamcheon-culture-village",
        "en": "Gamcheon Culture Village: visiting respectfully",
        "zh": "甘川文化村：尊重居民的旅行方式",
        "angle_en": "Walkable route, slopes and steps, local history, quiet photo etiquette",
        "angle_zh": "步行路線、坡道與階梯、在地歷史、拍照禮儀",
        "sources": ["https://www.visitbusan.net/"]
    },
    {
        "slug": "haeundae-blueline-park",
        "en": "Haeundae Blueline Park: Beach Train vs. Sky Capsule",
        "zh": "海雲臺藍線公園：海岸列車與天空膠囊比較",
        "angle_en": "Routes, ticket types, current operating calendar, official booking",
        "angle_zh": "路線、票種、最新營運日程、官方預訂",
        "sources": ["https://www.bluelinepark.com/", "https://www.visitbusan.net/"]
    },
    {
        "slug": "nampo-market-walk",
        "en": "Nampo-dong market walk: first-timer tips",
        "zh": "南浦洞市場散步：新手旅行實用提示",
        "angle_en": "Walking route between BIFF Square and nearby markets; transit and opening-hour checks",
        "angle_zh": "BIFF廣場與周邊市場步行路線、交通和營業時間確認",
        "sources": ["https://www.visitbusan.net/"]
    },
    {
        "slug": "busan-rainy-day",
        "en": "Busan rainy-day itinerary ideas",
        "zh": "釜山雨天備案行程",
        "angle_en": "Indoor alternatives and transport options; weather-dependent and seasonal details",
        "angle_zh": "室內備案和大眾運輸選項；確認季節與天氣資訊",
        "sources": ["https://www.visitbusan.net/"]
    },
    {
        "slug": "busan-family-transport",
        "en": "Busan transport with kids: planning checklist",
        "zh": "帶孩子玩釜山：交通規劃清單",
        "angle_en": "Subway and bus basics, stroller practicality, rest stops",
        "angle_zh": "地鐵與公車、嬰兒車實用性、休息站安排",
        "sources": ["https://www.visitbusan.net/"]
    },
    {
        "slug": "songdo-coast",
        "en": "Songdo coast: a flexible day trip outline",
        "zh": "松島海岸：彈性一日遊提案",
        "angle_en": "Public transportation, scenic stops, checking conditions and ticket prices",
        "angle_zh": "大眾運輸、觀景景點、票價與現場狀況確認",
        "sources": ["https://www.visitbusan.net/"]
    }
]
year, week, weekday = date.isocalendar()
topic = topics[(week - 1) % len(topics)]
folder = Path(__file__).resolve().parents[1] / "drafts"
folder.mkdir(parents=True, exist_ok=True)
path = folder / f"{date.isoformat()}-{topic['slug']}.md"
if path.exists():
    print(f"Already exists: {path.name}")
    sys.exit(0)
sources = "\n".join(f"- {url}" for url in topic["sources"])
content = f"""---
status: NEEDS_HUMAN_REVIEW
date: {date.isoformat()}
topic: {topic['slug']}
languages: [en, zh-Hant]
---

# WEEKLY EDITORIAL DRAFT — NOT FOR PUBLICATION

This is a topic and bilingual editorial outline, NOT an AI-written or independently
fact-checked article. No posting to the public website occurs from this file.
Add first-hand experience and/or licensed original photos before publishing.

## English title
{topic['en']}

### Editorial brief
{topic['angle_en']}

### Article outline (fill in after source review)
- Hook: who should visit, what problem this helps solve
- Practical itinerary or decision comparison
- Current directions and transport, checked against official source
- Accessibility, child-friendliness and on-site etiquette where relevant
- Last verified date and original photo credits
- Clear disclosure of any affiliate links (only after approval)

## 繁體中文標題
{topic['zh']}

### 編輯重點
{topic['angle_zh']}

### 文章架構（核對來源後填寫）
- 文章開頭：適合哪些旅客，解決什麼問題
- 景點與交通路線、時間安排
- 官方票價、訂票與營業資訊（請再次核對）
- 行動不便者及親子旅遊提醒
- 最後查證日期、照片著作權
- 分潤連結揭露（聯盟計畫獲准後才使用）

## Official sources for verification
{sources}

## Before publishing
- [ ] Verify times, prices, route and closures with official sources
- [ ] Review English and Traditional Chinese phrasing
- [ ] Add unique observations and self-shot/licensed visuals
- [ ] Remove unsourced details and add source links
- [ ] Verify any affiliate account and the disclosure
- [ ] Approve manually before publishing
"""
path.write_text(content, encoding="utf-8")
print(f"Created editorial review draft: {path.relative_to(folder.parent)}")
