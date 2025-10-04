from dataclasses import dataclass
from dotenv import load_dotenv
import os

@dataclass
class Settings:
BOT_TOKEN: str

def load_settings(required=("BOT_TOKEN",)):
load_dotenv()
missing = [k for k in required if not os.getenv(k)]
if missing:
raise RuntimeError(f"Missing env keys: {', '.join(missing)}")
return Settings(BOT_TOKEN=os.getenv("BOT_TOKEN", ""))
