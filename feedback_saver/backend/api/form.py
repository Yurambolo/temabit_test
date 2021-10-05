from aiohttp import web
import aiohttp_jinja2
from backend.db import save_message, check_portal_id, get_chat_id
from backend.bot import send_message_to_telegram


def get_form(request: web.Request):
    """
    ---
    tags:
    - Form
    produces:
    - text/plain
    responses:
        "200":
            description: successful operation. Return feedback form
    """
    response = aiohttp_jinja2.render_template('form.html', request, dict())
    return response


async def post_form(request: web.Request):
    """
    ---
    tags:
    - Form
    produces:
    - text/plain
    parameters:
        - in: path
          name: portal_id
          type: integer
          format: int64
          description: portal id
          required: false
        - in: body
          name: text
          description: Message text
          required: true
          type: string
    responses:
        "200":
            description: successful operation. Return feedback form
    """
    portal_id = request.match_info.get('portal_id', None)
    data = await request.post()
    text = data['text']
    connection = request.app['db_connection']
    portal_id = await check_portal_id(connection, portal_id)
    await save_message(connection, portal_id, text)
    chat_id = await get_chat_id(connection, portal_id)
    send_message_to_telegram(chat_id, text)
    response = aiohttp_jinja2.render_template('form.html', request, dict())
    return response
