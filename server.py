# -*- coding: utf-8 -*-
# Copyright (c) 2015–2016 Molly White
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import tweepy
import requests
import json
import random
from time import gmtime, strftime


# ====== Individual bot configuration ==========================
bot_username = '@worthit_iam'
logfile_name = bot_username + ".log"

# ==============================================================


def create_tweet():
  """Create the text of the tweet you want to send."""
  # Replace this with your code!
  
  bird_response = requests.get('https://botwiki.org/api/corpora/data/animals/birds_north_america.json')
  the_birds = bird_response.json()
  bird_list = []
  
  for f in the_birds['birds']:
    for bird in f['members']:
      bird_list.append(bird)

  n = random.randint(0,len(bird_list))
  the_bird = bird_list[n]

  plant_response = requests.get('https://botwiki.org/api/corpora/data/plants/plants.json')
  the_plants = plant_response.json()
  plant_list = []

  for p in the_plants['instruments']:
    plant_list.append(p['name'])

  m = random.randint(0,len(plant_list))
  the_plant = plant_list[m]

  the_saying = "A %s in the hand is worth two in the %s" % (the_bird,the_plant)
  
  return the_saying


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