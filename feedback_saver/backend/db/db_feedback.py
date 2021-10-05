import aiopg
from config_loader import load_module_config


async def check_portal_id(connection: aiopg.Pool, portal_id):
    async with connection.acquire() as conn:
        cur = await conn.cursor()
        select = f"""
            SELECT portal_id FROM portals
            WHERE portal_id = '{portal_id}'
        """
        try:
            await cur.execute(select)
            chat_id = (await cur.fetchone())[0]
        except:
            chat_id = None
        if not chat_id:
            config = load_module_config(None, "telegram_bot")
            chat_id = config['default_portal_id']
        return chat_id


async def save_message(connection: aiopg.Pool, portal_id, text):
    async with connection.acquire() as conn:
        cur = await conn.cursor()
        insert_soundtrack = f"""
            INSERT INTO messages (text, portal_id)
            VALUES ('{text}', '{portal_id}')
        """
        await cur.execute(insert_soundtrack)


async def get_chat_id(connection: aiopg.Pool, portal_id):
    async with connection.acquire() as conn:
        cur = await conn.cursor()
        select = f"""
            SELECT chat_id FROM portals
            WHERE portal_id = '{portal_id}'
        """
        await cur.execute(select)
        chat_id = (await cur.fetchone())[0]
        return chat_id
