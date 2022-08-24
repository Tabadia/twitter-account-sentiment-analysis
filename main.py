# IMPORTS
import nltk
from colorama import init, Fore, Style
from nltk.sentiment import SentimentIntensityAnalyzer
import tweepy
from dotenv import load_dotenv
import os
import time
nltk.download('vader_lexicon')
init()
os.system("cls" or "clear")
load_dotenv()

# INTRODUCTION
print(Style.BRIGHT)
print(Fore.BLUE)
print("Welcome to the Twitter Account Sentiment Analyzer!")

# TWITTER API AUTHENTICATION
print(Fore.BLUE)
username=input('Enter a username: ')
print(Fore.WHITE)
print("Accessing Twitter API... (This may take a while)")
auth = tweepy.OAuthHandler(os.getenv('key1'), os.getenv('key2'))
auth.set_access_token(os.getenv('key3'), os.getenv('key4'))
api = tweepy.API(auth, wait_on_rate_limit=True)
tweets_list = []
for tweet in tweepy.Cursor(api.user_timeline, screen_name=username, count=None, tweet_mode='extended', exclude_replies=True, include_rts=False).items(500):
  tweets_list.append(tweet)

# SENTIMENT ANALYSIS
print(Fore.BLUE)
print("Calculating...")
print(Fore.WHITE)
print(f"Tweets found: {len(tweets_list)}")
sia = SentimentIntensityAnalyzer()
pos = 0
neg = 0
neu = 0
total = 0

for tweet in tweets_list:
  total += 1
  result = sia.polarity_scores(tweet.full_text)
  if result['pos'] > result['neg']:
    pos += 1
  elif result['neg'] > result['pos']:
    neg += 1
  elif result['neu'] > 0.2:
    neu += 1
  else:
    total -= 1

# OUTPUT
neu = neu/total
pos = pos/total
neg = neg/total
print(Fore.BLUE)
print(f"Positive: {round(pos*100,2)}% \nNegative: {round(neg*100,2)}% \nNeutral: {round(neu*100,2)}%")

input("\n\n\nPress esc to exit...")
time.sleep(10)