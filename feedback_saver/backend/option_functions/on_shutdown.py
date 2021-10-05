async def close_db_connection(app):
    connection = app['db_connection']
    connection.close()