import asyncio
import sys
from app.settings import setup

from aiohttp import web

if sys.version_info >= (3, 8) and sys.platform.lower().startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

if __name__ == '__main__':
    app = web.Application()
    setup(app)
    web.run_app(app)
