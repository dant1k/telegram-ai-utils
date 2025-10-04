from tg_utils.env import load_settings
from tg_utils.logging import setup_logging
from tg_utils.ratelimit import RateLimitMiddleware

def test_imports():
    assert callable(setup_logging)
    assert RateLimitMiddleware(0.5) is not None
