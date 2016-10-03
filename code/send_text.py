# imports
from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "get from twilo site" 
AUTH_TOKEN = "get from twilo site"
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
phoneNumbers = client.phone_numbers.search(
	country="AU",  
	type="mobile"
) 
 
for p in phoneNumbers: 
	print p.phone_number
