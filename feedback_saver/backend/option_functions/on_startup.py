import aiohttp_jinja2
import jinja2
from aiopg import create_pool
from config_loader import load_module_config
from aiohttp_swagger import setup_swagger

from backend.api import form_routes


async def init_routes(app):
    """
     Init routes application
    :param app: aiohttp.Application
    :return: None
    """
    for route in form_routes:
        app.router.add_route(
            method=route[0],
            path=app["settings"].DOMAIN_URL_REQUEST + route[1],
            handler=route[2],
            name=route[3],
        )
    app.logger.info("Init routes")


async def init_jinja(app):
    """
     Init jinja application
    :param app: aiohttp.Application
    :return: None
    """
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(app["settings"].TEMPLATES_DIR))
    app.logger.info("Init jinja")


async def init_db_connection(app):
    config = load_module_config(None, "database_local")
    dsn = f'dbname={app["settings"].DB_NAME} user={config["user"]} password={config["password"]} host={config["host"]}'
    connection = await create_pool(dsn)
    app['db_connection'] = connection


async def init_swagger(app):
    setup_swagger(app)
