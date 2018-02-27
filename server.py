# -*- coding: utf-8 -*-

import requests
import urllib
import os
import tweepy

def tweet(file,text):
  """Send out the text as a tweet."""
  # Twitter authentication
  auth = tweepy.OAuthHandler(os.environ['C_KEY'], os.environ['C_SECRET'])
  auth.set_access_token(os.environ['A_TOKEN'], os.environ['A_TOKEN_SECRET'])
  api = tweepy.API(auth)

  api.update_with_media(file,text)
  
def tweet_image():
    filename = urllib.urlopen('https://kotofoto.ru/UserFiles/Image/category/3100/138527_vinilovaya_plastinka_joy_division_unknown_pleasuresm.jpg')
    #filename = 'e813cbb64ced5d7d8cc24a0789720729.jpg'
    text = "Hello!"
    
    return filename,text

if __name__ == "__main__":
  image,text = tweet_image()
  tweet(image,text)
  