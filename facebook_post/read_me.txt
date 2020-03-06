create App using -
https://developers.facebook.com/apps

1. Uninstall existing packages and install Facebook SDK

sudo pip uninstall facebook
sudo pip uninstall facebook-sdk
sudo pip install facebook-sdk


2. Get the "User Access Token"

Open following URL-

https://developers.facebook.com/tools/explorer/

a. From "Application" drop down button select "Graph API Explorer"
b. From "Get Token" drop down button select "Get User Access Tocken"
c. A Dialogue Bos must appear after this. Click on "Extended Permissions" and select "publish_actions"
d. Click on "Get Access Tocken"
e. Follow the instructions after that and allow it to post on your FB Page.
f. Once the process gets completed, copy the token from "Access Token:" text box and save it in settings file.


3. Once you get "User Access Tocken" cross check App permissions in you FB Profile
a. Login to your FB Account 
b. Go to Settings
c. Click on Apps to see the registered app and Permissions


4. Convert this short term "User Access Tocken" into "Long Term Token" using following url (This tocken will exprire in 60 Days) -
Save it in "FB_ACCESS_TOKEN" setting under "FACEBOOK" settings

https://graph.facebook.com/oauth/access_token?client_id=<APP_ID>&client_secret=<APP_SECRET>&grant_type=fb_exchange_token&fb_exchange_token=<EXISTING_ACCESS_TOKEN>

easy to read format -

https://graph.facebook.com/oauth/access_token?
  client_id=<APP_ID>&
  client_secret=<APP_SECRET>&
  grant_type=fb_exchange_token&
  fb_exchange_token=<EXISTING_ACCESS_TOKEN>
  
  
  
  
Reference:
=============
http://nodotcom.org/python-facebook-tutorial.html



  