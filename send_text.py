# imports
from twilio import rest
 
# put your own credentials here 
ACCOUNT_SID = "get from twilo site" 
AUTH_TOKEN = "get from twilo site"
 
client = rest.TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
message = client.messages.create(
    body="Hello from Python", # Text to send
    to="+123456",    # Replace with your phone number
    from_="+987654") # Replace with your Twilio number

print(message.sid)