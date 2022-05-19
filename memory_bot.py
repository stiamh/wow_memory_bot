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
import glob
from PIL import Image

image_list = []
folderpath = "Python Practice/wow_memory_bot/Screenshots"

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


# def test_tweet(api):
#     test = api.update_status("Test upload")
#     print(test)

def tweet_picture(api):
    for picture in glob.glob(folderpath):
        try:
            image = Image.open(picture)
            api.media_upload(picture)
            print("Tweeted!")
            image_list.append(image)
            sleep(900)
            print(image_list)
        except Exception as e:
            print("encountered error! error deets: %s"%str(e))
            break

tweet_picture(api)
