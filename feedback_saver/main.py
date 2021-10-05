"""
Module for run web app
"""
import asyncio
import sys

from aiohttp import web
from graylogger import init_graylogger

from backend import init_app

logger = init_graylogger()


if "win" in str(sys.platform):
    logger.info("Used standard loop")
else:
    try:
        import uvloop

        uvloop.install()
        logger.info("Used uvloop")
    except ModuleNotFoundError:
        logger.info("Used standard loop")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init_app(loop, log=logger))
    web.run_app(app)
