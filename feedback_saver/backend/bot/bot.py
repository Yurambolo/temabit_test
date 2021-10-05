import requests
from config_loader import load_module_config

METHOD_URL = r'sendMessage'
REQUEST_URL = "https://api.telegram.org/bot{0}/{1}"


def send_message_to_telegram(chat_id, text):
    config = load_module_config(None, "telegram_bot")
    request_url = REQUEST_URL.format(config['token'], METHOD_URL)
    payload = {'chat_id': str(chat_id), 'text': text}
    requests.post(request_url, payload)
