import asyncio
import os

from aiohttp import web
from graylogger import init_graylogger
from werkzeug.utils import import_string
from aiohttp_swagger import setup_swagger

from .option_functions import init_routes, init_jinja, init_db_connection, close_db_connection
import sys

settings = import_string(os.getenv("APP_SETTINGS", "backend.settings.DevSettings"))


async def init_app(loop=None, log=None):
    if not log:
        log = init_graylogger()
    if not loop:
        if "win" in str(sys.platform):
            log.info("Used standard loop")
        else:
            try:
                import uvloop

                uvloop.install()
                log.info("Used uvloop")
            except ModuleNotFoundError:
                log.info("Used standard loop")
        loop = asyncio.get_event_loop()

    app = web.Application(
        logger=log
    )
    app["loop_app"] = loop
    app["settings"] = settings

    app.on_startup.append(init_routes)
    app.on_startup.append(init_jinja)
    app.on_startup.append(init_db_connection)
    app.on_shutdown.append(close_db_connection)
    setup_swagger(app)
    return app
