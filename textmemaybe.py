from twilio.rest import Client
import os
import random

# Env variables to py variables
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
from_num = os.getenv('TWILIO_NO')
to_num = os.getenv('MY_NO')
                
# Open client- we're in
client = Client(account_sid, auth_token)

# List o messages
with open("guyisms.txt","r") as f:
    quotes = f.read().splitlines()
# pick one
body = random.choice(quotes)

# SEND. greetings from flavorland, yall
message = client.messages \
    .create(
         body=body,
         from_=from_num,
         to=to_num
     )

