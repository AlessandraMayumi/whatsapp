import requests
import os
import logging

from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.DEBUG,
                    format=f'[%(asctime)s] [%(levelname)s] [%(name)s] [%(threadName)s] %(message)s')
log = logging.getLogger('api')

baseUrl = os.getenv("SERVER_ENDPOINT")


def create_gift(chat):
    payload = {
        "title": chat['gift'],
        "description": chat['gift'],
        "status": "TO_APPROVE",
        "kidInformation": {
            "name": chat['name'],
            "phone": chat['from'].replace("whatsapp:+", ""),
            "address": chat['address'],
        }
    }
    try:
        requests.post(baseUrl, data=payload)
    except Exception as e:
        log.error(e.__str__())
        pass
