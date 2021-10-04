import os

from aiopg import create_pool
from aiohttp_swagger import *
from config_loader import load_module_config
from graylogger import init_graylogger

from api.urls import urls

os.environ["CFG_file"] = "config.yaml"
DB_NAME = 'test_async_db'


def setup(app):
    app.logger = init_graylogger()
    app.on_startup.append(init_connect)
    app.on_shutdown.append(close_connection)
    app.add_routes(urls)
    setup_swagger(app)


async def init_connect(app):
    config = load_module_config(None, "database_local")
    dsn = f'dbname={DB_NAME} user={config["user"]} password={config["password"]} host={config["host"]}'
    connection = await create_pool(dsn)
    app['db_connection'] = connection


async def close_connection(app):
    connection = app['db_connection']
    connection.close()
