from twilio.rest import Client

f = open("token.password", "r")
token = f.readline()
f.close()


account_sid = 'AC23891757669d832bdd5ad158c530548a'
auth_token = token
client = Client(account_sid, auth_token)

while True:
    textMessage = input("What you would like to send?: ")
    numberToBeSent = input("Where you want to send your message?: ")

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=textMessage,
        to=f'whatsapp:{numberToBeSent}'
    )

    print(message.sid)
