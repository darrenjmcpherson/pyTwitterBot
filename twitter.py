import tweepy
import time
from twitter_keys import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()

search = 'JavaScript'
no_of_tweets = 20

for tweet in tweepy.Cursor(api.search, search).items(no_of_tweets):
    try:
        print('tweet liked')
        tweet.favorite()
        #tweet.retweet() - if you want to do retweets.
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break