# WARNING: the code that follows will make you cry; a safety pig is provided below for your benefit.
#
#                          _
#  _._ _..._ .-',     _.._(`))
# '-. `     '  /-._.-'    ',/
#    )         \            '.
#   / _    _    |             \
#  |  a    a    /              |
#  \   .-.                     ;
#   '-('' ).-'       ,'       ;
#      '-;           |      .'
#         \           \    /
#         | 7  .__  _.-\   \
#         | |  |  ``/  /`  /
#        /,_|  |   /,_/   /
#           /,_/      '`-'
import tweepy
from time import sleep
import os
from dotenv import load_dotenv

# Opens the .env file with keys 
load_dotenv()
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

twitter_auth_keys = {
        "consumer_key" : consumer_key,
        "consumer_secret" : consumer_secret,
        "access_token" : access_token,
        "access_token_secret" : access_token_secret
}

auth = tweepy.OAuthHandler(
        twitter_auth_keys["consumer_key"],
        twitter_auth_keys["consumer_secret"]
        )
auth.set_access_token(
        twitter_auth_keys["access_token"],
        twitter_auth_keys["access_token_secret"]
        )
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

def tweet_picture(api):
    os.chdir('screenshots')
    for screenshot in os.listdir('.'):
        tweet = "✨🦉✨"
        media = api.media_upload(screenshot)
        api.update_status(status=tweet, media_ids=[media.media_id])
        print("Image Tweeted!")
        sleep(43200) # 43200 seconds = 1 day
    tweet_picture(api) # Loops back to the beginning when finished. 

tweet_picture(api)
