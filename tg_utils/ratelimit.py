import time
from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any, Awaitable

class RateLimitMiddleware(BaseMiddleware):
def init(self, per_user_seconds: float = 1.0):
super().init()
self.per_user_seconds = per_user_seconds
self._last: Dict[int, float] = {}
async def __call__(self, handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], event: Message, data: Dict[str, Any]):
    uid = event.from_user.id if event.from_user else 0
    now = time.time()
    last = self._last.get(uid, 0)
    if now - last < self.per_user_seconds:
        return
    self._last[uid] = now
    return await handler(event, data)

