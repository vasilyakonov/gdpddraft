# -*- coding: utf-8 -*-

import requests
import os
import tweepy
import shutil
import PIL

def tweet(file,text):
  """Send out the text as a tweet."""
  # Twitter authentication
  auth = tweepy.OAuthHandler(os.environ['C_KEY'], os.environ['C_SECRET'])
  auth.set_access_token(os.environ['A_TOKEN'], os.environ['A_TOKEN_SECRET'])
  api = tweepy.API(auth)

  api.update_with_media(file,text)
  # you should read the img directory and delete file after posting
  
def tweet_image():
    url = 'https://is2-ssl.mzstatic.com/image/thumb/Purple118/v4/7d/5a/a0/7d5aa0d4-5b31-1f54-65cf-aa6588984c96/pr_source.jpg/200x0w.jpg'
    response = requests.get(url, stream=True)
     #you shold be able to specify a path, check glitch support for writing to ASSETS or to .tmp folder
    with open('img.jpg', 'wb') as out_file:
      shutil.copyfileobj(response.raw, out_file)
      from PIL import Image, ImageDraw

      im = Image.open("img.jpg")

      draw = ImageDraw.Draw(im)
      draw.line((0, 0) + im.size, fill=128)
      draw.line((0, im.size[1], im.size[0], 0), fill=128)
      del draw

# write to stdout
      im.save(sys.stdout, "JPG")
      del response
    filename = 'img.jpg'
    text = "Yes!"
    
    return filename,text

if __name__ == "__main__":
  image,text = tweet_image()
  tweet(image,text)
  