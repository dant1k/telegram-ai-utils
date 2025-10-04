from tg_utils.ratelimit import RateLimitMiddleware

def test_ratelimit_constructs():
    m = RateLimitMiddleware(0.2)
    assert hasattr(m, "_last")
