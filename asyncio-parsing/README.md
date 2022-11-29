# AsyncIO parser with redis and docker-compose

## Description
With this service you can get a news async aggregator (links.py) with redisDB as a key/value storage and docker-compose config. 

## Installation
1. !git clone https://github.com/alexfomin1/asyncio-parsing.git
2. !cd asyncio-parsing
3. !docker-compose up -d --build

## Stack
- python3.10
- docker
- asyncio
- feedparser
- redisDB -> aioredis
- loguru
