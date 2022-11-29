import asyncio
import sys

from loguru import logger
from pydantic import ValidationError

import redising
from models import Article_redis
import aioredis
import redis

logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")


async def validate_data_redis(source, link):
    try:
        Article_redis(source=source, link=link)
    except ValidationError:
        logger.error("Data for redis is INVALID!")
        return False
    return True


async def check_value_redis(source: str, link: str):
    if validate_data_redis(source=source, link=link):
        redis = await aioredis.from_url("redis://localhost:6379/0")
        s = await redis.exists(source, link)
        await redis.close()
        return s
