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

#API KEY = hy0BkQlIxWqyCtEPcAx4CfEMs
#SECRET API KEY = EwMeBsrgtLSvRBlGymDy2sei5Qn5g5qfA8c9aNGBZU3gxmJkTY
#BEARER TOKEN = AAAAAAAAAAAAAAAAAAAAADuObAEAAAAA4Gfw%2FCZNaJK7Ym07Q9qAgAtMBck%3DDfteKBUK57mSphb4We4wZ5lBWn3OsikrhqIzqampbDKxfqWflu
#ACCESS TOKEN = 1028632935946174465-BL7XHw9YdPVbx4M1RXUKMfRMfW7pOQ
#ACCESS SECRET TOKEN = EQmDK4ZdYVkQn6CYgHUa1GnyrLDbQfdanJAYmdToKxNWM

#Client ID = YVJMaG5xNzF4OFRVcmVOQU5FUko6MTpjaQ
#Client Secret = 2jx_sniL_qH9AH4SS7bMXFiFC-DQq5nD1QcmIzxnC_fczZL4cj FOR OAuth 2.0
import tweepy
from time import sleep
from pathlib import Path
import os

twitter_auth_keys = {
        "consumer_key" : "hy0BkQlIxWqyCtEPcAx4CfEMs",
        "consumer_secret" : "EwMeBsrgtLSvRBlGymDy2sei5Qn5g5qfA8c9aNGBZU3gxmJkTY",
        "access_token" : "1028632935946174465-BL7XHw9YdPVbx4M1RXUKMfRMfW7pOQ",
        "access_token_secret" : "EQmDK4ZdYVkQn6CYgHUa1GnyrLDbQfdanJAYmdToKxNWM"
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
