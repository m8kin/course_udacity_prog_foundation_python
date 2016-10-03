# imports
from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "ACce29b565248e092c7dd87a73990689e4" 
AUTH_TOKEN = "a5fca2fdfa79ed32612d3f5bc05f49e4" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
phoneNumbers = client.phone_numbers.search(
	country="AU",  
	type="mobile"
) 
 
for p in phoneNumbers: 
	print p.phone_number
