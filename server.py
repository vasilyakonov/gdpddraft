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
  
def tweet_image():
    url = 'https://kotofoto.ru/UserFiles/Image/category/3100/138527_vinilovaya_plastinka_joy_division_unknown_pleasuresm.jpg'
    response = requests.get(url, stream=True)
    with open('img.jpg', 'wb') as out_file:
      shutil.copyfileobj(response.raw, out_file)
      del response
    # filename = urllib.urlopen('https://kotofoto.ru/UserFiles/Image/category/3100/138527_vinilovaya_plastinka_joy_division_unknown_pleasuresm.jpg')
    filename = 'img.jpg'
    text = "Hello!"
    
    return filename,text

if __name__ == "__main__":
  image,text = tweet_image()
  tweet(image,text)
  