from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell_number,my_twilio_number

client = Client(account_sid, auth_token)

my_message = ''.join(['what\'s up !man \n' for i in range(10)])


message = client.messages.create(to=my_cell_number,from_=my_twilio_number,body=my_message)

print(message)