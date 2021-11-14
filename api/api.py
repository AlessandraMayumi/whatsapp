import requests
import os
import logging

from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.DEBUG,
                    format=f'[%(asctime)s] [%(levelname)s] [%(name)s] [%(threadName)s] %(message)s')
log = logging.getLogger('api')

baseUrl = os.getenv("SERVER_ENDPOINT")


def api_create_gift(chat):
    payload = {
        "title": f'"{chat["gift"]}"',
        "description": f'"{chat["gift"]}"',
        "status": "TO_APPROVE",
        "kidInformation": {
            "name": f'"{chat["name"]}"',
            "phone": f'"{chat["from"].replace("whatsapp:+", "")}"',
            "address": f'"{chat["address"]}"'
        }
    }
    try:
        log.info(payload)
        requests.post(f'{baseUrl}/gifts', data=payload)
    except Exception as e:
        log.error(e.__str__())
        pass
