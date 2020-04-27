from twilio.rest import Client

client = Client('ACCOUNT_SID', 'AUTH_TOKEN')

message = client.messages \
    .create(
         body='HELP HELP',
         from_='TWILIO_NO',
         to='MY_NO'
     )

