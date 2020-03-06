from twitter import *
from settings.parseSettings import get_Settings

TWITTER_Settings = get_Settings('TWITTER')
CONSUMER_KEY=TWITTER_Settings['CONSUMER_KEY']
CONSUMER_SECRET=TWITTER_Settings['CONSUMER_SECRET']
ACCESS_TOKEN=TWITTER_Settings['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET=TWITTER_Settings['ACCESS_TOKEN_SECRET']

def publish_Status_On_Twitter(Twitter_Status):
	TW = Twitter(auth=OAuth(ACCESS_TOKEN,ACCESS_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET))
	TW.statuses.update(status=Twitter_Status)
	

