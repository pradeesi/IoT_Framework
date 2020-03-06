import facebook
from settings.parseSettings import get_Settings

FACEBOOK_Settings = get_Settings('FACEBOOK')
FB_APP_ID=FACEBOOK_Settings['FB_APP_ID']
FB_APP_SECRET=FACEBOOK_Settings['FB_APP_SECRET']
FB_ACCESS_TOKEN=FACEBOOK_Settings['FB_ACCESS_TOKEN']

def post_on_Facebook(strMsg):
	facebook_graph = facebook.GraphAPI(FB_ACCESS_TOKEN)
	try:
		response = facebook_graph.put_wall_post(strMsg)
	except facebook.GraphAPIError as e:
		print e
	
	


