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
        sleep(43200)
        print("Image Tweet!")
    tweet_picture(api)

tweet_picture(api)
