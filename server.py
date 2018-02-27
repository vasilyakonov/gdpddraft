# -*- coding: utf-8 -*-

import os
import tweepy
import requests
import json
import random
from time import gmtime, strftime


# ====== Individual bot configuration ==========================
bot_username = '@XmrpibbX'
logfile_name = bot_username + ".log"
# ==============================================================

def create_tweet():
  """Create the text of the tweet you want to send."""
  # Replace this with your code!
  
  municipalities_response = requests.get('https://botwiki.org/api/corpora/data/geography/canadian_municipalities.json')
  the_municipalities = municipalities_response.json()
  municipalities_list = []
  
  for f in the_municipalities["municipalities"]:
    for municipalities in f["name"]:
     for municipalities in f["province"]:
      #for municipalities in f["type"]:
       #for municipalities in f["population"]:
       municipalities_list.append(municipalities)

  n = random.randint(0,len(municipalities_list))
  the_municipality = municipalities_list[n]

  plant_response = requests.get('https://botwiki.org/api/corpora/data/plants/plants.json')
  the_plants = plant_response.json()
  plant_list = []

  for p in the_plants['instruments']:
    plant_list.append(p['name'])

  m = random.randint(0,len(plant_list))
  the_plant = plant_list[m]

  the_tweet = "A %s samiyam commencement %s" % (the_municipality,the_plant)
  
  
  
  return the_tweet


def tweet(text):
  """Send out the text as a tweet."""
  # Twitter authentication
  auth = tweepy.OAuthHandler(os.environ['C_KEY'], os.environ['C_SECRET'])
  auth.set_access_token(os.environ['A_TOKEN'], os.environ['A_TOKEN_SECRET'])
  api = tweepy.API(auth)

  # Send the tweet and log success or failure
  # try:
  api.update_status(text)
  # except tweepy.error.TweepError as e:
    # log(e.message)
  # else:
    # log("Tweeted: " + text)

# def log(message):
#   """Log message to logfile."""
#   path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
#   with open(os.path.join(path, logfile_name), 'a+') as f:
#     t = strftime("%d %b %Y %H:%M:%S", gmtime())
#     f.write("\n" + t + " " + message)

if __name__ == "__main__":
  tweet_text = create_tweet()
  tweet(tweet_text)