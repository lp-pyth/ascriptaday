import tweepy
from tweepy import OAuthHandler
import pandas as pd

consumer_key = '321mdmn@gmail.com'
consumer_secret = '321.Marshall'
access_token = 'access_token'
access_secret = 'access_secret'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

api = tweepy.API(auth)
screen_name='screen_name'
tweets = api.user_timeline(screen_name, count=200, include_rts=False)
save=['']*len(tweets)

for i in range(len(tweets)):
    save[i]=tweets[i].text
    print(tweets[i].text)

data = pd.DataFrame(save)
