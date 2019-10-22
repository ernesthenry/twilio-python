from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "XXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token = "XXXXXXXXXX"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+256701391909",
    from_="+14154172879",
    body="Hello from heradcloud! Visit our website at https://heradcloud.tk/")

print(message.sid)

