from twilio.rest import Client

f = open("token.password", "r")
token = f.readline()
f.close()


account_sid = 'AC23891757669d832bdd5ad158c530548a'
auth_token = token
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Your appointment is coming up on July 21 at 3PM',
    to='whatsapp:+905395740062'
)

print(message.sid)