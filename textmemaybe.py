from twilio.rest import Client
import os

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
from_num = os.getenv('TWILIO_NO')
to_num = os.getenv('MY_NO')
                

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='HELP HELP',
         from_=from_num,
         to=to_num
     )

