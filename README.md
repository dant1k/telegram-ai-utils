# telegram-ai-utils
Small, reusable helpers for Telegram bots (Aiogram 3.x): logging, env loader, and rate-limit middleware.
## Install
```bash
pip install -r requirements.txt
What’s inside

env.py – .env loader with required/optional keys

logging.py – pretty logging setup

ratelimit.py – per-user rate limiter (middleware)

example.py – tiny bot to show how it plugs in
