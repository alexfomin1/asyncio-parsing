import asyncio
import aioredis
import sys
from loguru import logger


logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")


async def main():
    redis = await aioredis.from_url("redis://localhost:6379/0", decode_responses=True)
    l = await redis.keys()
    for i in l:
        print(i, await redis.get(i))
    await redis.close()


if __name__ == "__main__":
    asyncio.run(main())
