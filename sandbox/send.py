import os
import logging
from twilio.rest import Client
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG, format=f'[%(asctime)s] [%(levelname)s] [%(name)s] [%(threadName)s] %(message)s')
log = logging.getLogger('send')
load_dotenv()

# [Twilio console] Account - General settings
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)


def send_one_way_message():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Message from Python',
        to='whatsapp:+5519989711675'
    )

    log.info(message.sid)
