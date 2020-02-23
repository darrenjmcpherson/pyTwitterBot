import tweepy
import time
from twitter_keys import API_KEY, API_SECRET_KEY

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)