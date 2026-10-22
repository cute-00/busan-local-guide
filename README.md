# Busan Local Guide

A small experimental bilingual travel-information site (English / Traditional Chinese).

## Public website

https://cute-00.github.io/busan-local-guide/

GitHub Pages publication requires **Settings → Pages → Source: GitHub Actions**.
Successful Actions deployment does not itself guarantee independent site verification.

## What's implemented

- `index.html`: bilingual landing page and two introductory travel guides
- `.github/workflows/deploy.yml`: publishes the site on changes to `main`
- `scripts/create_draft.py`: produces a bilingual editorial outline and fact-check list from curated topics
- `.github/workflows/weekly-draft.yml`: runs every Monday at 09:00 Korea Standard Time, saving a **review-only** draft to `drafts/`

The weekly draft generator uses prewritten topic briefs, **not an AI content service**. It does not automatically publish drafts or fetch live travel data. GitHub scheduled runs may be delayed and can be disabled after prolonged repository inactivity.

## What is not yet implemented

- Verified Klook or other affiliate account; no revenue tracking link
- Automated publication to Instagram or Pinterest
- Automatic AI article writing, translation checking, original photos or current price/timetable validation
- Analytics, consent/privacy policies and commercial disclosures beyond the current launch statement
- Proven traffic or revenue (current revenue: 0)

## Mobile checks

1. [Site](https://cute-00.github.io/busan-local-guide/)
2. [Deployment & scheduled workflows](https://github.com/cute-00/busan-local-guide/actions)
3. [Draft review queue](https://github.com/cute-00/busan-local-guide/tree/main/drafts) (available after first scheduled successful draft)

Do not store passwords, API tokens or affiliate account credentials in public repository files.
