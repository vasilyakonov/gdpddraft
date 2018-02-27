# -*- coding: utf-8 -*-

import requests
import os
import tweepy
import shutil

def tweet(file,text):
  """Send out the text as a tweet."""
  # Twitter authentication
  auth = tweepy.OAuthHandler(os.environ['C_KEY'], os.environ['C_SECRET'])
  auth.set_access_token(os.environ['A_TOKEN'], os.environ['A_TOKEN_SECRET'])
  api = tweepy.API(auth)

  api.update_with_media(file,text)
  # you should read the img directory and delete file after posting
  
def tweet_image():
    url = 'https://kotofoto.ru/UserFiles/Image/category/3100/138527_vinilovaya_plastinka_joy_division_unknown_pleasuresm.jpg'
    response = requests.get(url, stream=True)
    # you shold be able to specify a path, check glitch support for writing to ASSETS or to .tmp folder
    with open('img.jpg', 'wb') as out_file:
      shutil.copyfileobj(response.raw, out_file)
      del response
    filename = 'img.jpg'
    text = "Hello!"
    
    return filename,text

if __name__ == "__main__":
  image,text = tweet_image()
  tweet(image,text)
  