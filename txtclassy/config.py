import os

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Config(BaseSettings):
    # redis
    redis_url = os.getenv("REDIS_URL", default="redis://127.0.0.1:6379")
    redis_db = os.getenv("REDIS_DB", default=1)
