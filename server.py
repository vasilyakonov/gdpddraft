# -*- coding: utf-8 -*-

import requests
import os
import tweepy
import shutil
import pillow

def tweet(file,text):
  """Send out the text as a tweet."""
  # Twitter authentication
  auth = tweepy.OAuthHandler(os.environ['C_KEY'], os.environ['C_SECRET'])
  auth.set_access_token(os.environ['A_TOKEN'], os.environ['A_TOKEN_SECRET'])
  api = tweepy.API(auth)

  api.update_with_media(file,text)
  # you should read the img directory and delete file after posting
  
def tweet_image():
    #url = 'http://fscomps.fotosearch.com/compc/BNS/BNS389/hands-rubbing-mans-face-picture__bn300027.jpg'
    #esponse = requests.get(url, stream=True)
     ##you shold be able to specify a path, check glitch support for writing to ASSETS or to .tmp folder
    #with open('img.jpg', 'wb') as out_file:
      #shutil.copyfileobj(response.raw, out_file)
      #del response
      
    from PIL import Image
im = Image.new("RGB", (512, 512), "white")
saveImage(img.
  
  filename = 'img.jpg'
  text = "Yes!"
    
    return filename,text

if __name__ == "__main__":
  image,text = tweet_image()
  tweet(image,text)
  