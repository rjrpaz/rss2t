# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working
with code in this repository.

## What this project does

`rss2t` is a Python bot that polls RSS feeds and forwards new items to
Telegram channels. It runs as a one-shot process: reads all configured
feeds, sends any entries newer than the stored `last` timestamp, updates
that timestamp in `config.ini`, then exits.

## Setup

```bash
pip install -r requirements.txt
```

Copy `config.ini.sample` → `config.ini` and fill in your `bot_token` and
channel IDs. The `local_settings.py.sample` file in the package is a
legacy artifact; the real configuration lives entirely in `config.ini`.

## Running

```bash
python -m rss2t
```

Must be run from the project root so that `config.ini` is found at the
working directory (the path is hardcoded as `'config.ini'` in both
`rss2t/config.py` and `rss2t/telegram.py`).

## Adding a new feed

```bash
python utils/add_feed.py <TAG> <CHANNEL_TAG> <URL>
```

`CHANNEL_TAG` must already exist in the `[CHANNELS]` section of
`config.ini`.

## Linting

pylint is configured as a pre-push hook via pre-commit:

```bash
pre-commit run pylint       # run manually
pylint rss2t/ utils/        # or directly
```

## Architecture

| File | Role |
| --- | --- |
| `rss2t/__main__.py` | Entry point, calls `app.run()` |
| `rss2t/app.py` | Main loop: iterates feeds, checks timestamps, dispatches |
| `rss2t/config.py` | `Feed` class + `list_feeds()` — reads `config.ini` |
| `rss2t/telegram.py` | `send_message()` — POSTs to the Telegram Bot API |
| `utils/add_feed.py` | CLI helper to append a new feed section to `config.ini` |

**State management:** `config.ini` is both the configuration file and the
runtime state store. The `last` field in each feed section is updated
in-place after each run to record the Unix timestamp of the most recent
entry seen. A plain `configparser.ConfigParser` (no interpolation) is used
when writing, while `ExtendedInterpolation` is used when reading so that
`${CHANNELS:channel1}` references resolve correctly.

**config.ini structure:**

```ini
[DEFAULT]
bot_token = <telegram_bot_token>

[CHANNELS]
news = <telegram_channel_id>

[feed_tag]
last = 0
url = https://example.com/feed.rss
channel_id = ${CHANNELS:news}
```
