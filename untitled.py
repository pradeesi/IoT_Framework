from twitter import *


# Set the values for following variables from your Twitter Account
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

# This function will tweet
def publish_Status_On_Twitter(Twitter_Status):
	TW = Twitter(auth=OAuth(ACCESS_TOKEN,ACCESS_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET))
	TW.statuses.update(status=Twitter_Status)
	

publish_Status_On_Twitter("test")