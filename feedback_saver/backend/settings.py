from pathlib import Path
import os

BASE_DIR = Path(__file__).parent.parent


class AppSettings:
    """
    App Settings
    """

    IS_DEV = False
    DOMAIN_URL_REQUEST = ""
    BASE_DIR = BASE_DIR

    DB_NAME = 'feedback_saver_db'

    TEMPLATES_DIR = str(BASE_DIR) + os.sep + 'backend' + os.sep + 'templates'
    print(TEMPLATES_DIR)


class DevSettings(AppSettings):
    IS_DEV = True
