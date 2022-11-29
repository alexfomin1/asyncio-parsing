import asyncio
from loguru import logger
import sys

from links import list_of_links
from parser import parser
from checking_redis import validate_data_redis
import redising


logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")


async def main():
    while True:
        tasks = []
        for link in list_of_links:
            tasks.append(parser(link))
        for task in asyncio.as_completed(tasks):
            result = await task
            if result:
                await redising.analyze_redis(
                    source=result["source"], link=result["link"]
                )
        await redising.get_all_redis()
        print("=====================================")
        await asyncio.sleep(15)


if __name__ == "__main__":
    asyncio.run(main())
