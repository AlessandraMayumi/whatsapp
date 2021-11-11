import os
import logging
from twilio.rest import Client
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG, format=f'[%(asctime)s] [%(levelname)s] [%(name)s] [%(threadName)s] %(message)s')
log = logging.getLogger('send')
load_dotenv()


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there! Test Sample',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+5519989711675'
                          )

print(message.sid)
