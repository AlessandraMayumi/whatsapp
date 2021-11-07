import os
from twilio.rest import Client 
from dotenv import load_dotenv

load_dotenv()

# [Twilio console] Account - General settings
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your appointment is coming up on July 21 at 3PM',      
                              to='whatsapp:+5519989711675' 
                          ) 
 
print(message.sid)