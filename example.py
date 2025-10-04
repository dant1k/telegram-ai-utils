from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from tg_utils.env import load_settings
from tg_utils.logging import setup_logging
from tg_utils.ratelimit import RateLimitMiddleware
import asyncio

async def main():
settings = load_settings()
log = setup_logging()
bot = Bot(settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()
dp.message.middleware(RateLimitMiddleware(0.7))
@dp.message(F.text == "/ping")
async def ping(m: Message):
    await m.answer("pong")

log.info("Starting example bot")
await dp.start_polling(bot)

if name == "main":
asyncio.run(main())
