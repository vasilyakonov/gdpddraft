# -*- coding: utf-8 -*-

import requests
import os
import tweepy
import shutil
import PIL
import pip
import WCK


def tweet(file,text):
  """Send out the text as a tweet."""
  # Twitter authentication
  auth = tweepy.OAuthHandler(os.environ['C_KEY'], os.environ['C_SECRET'])
  auth.set_access_token(os.environ['A_TOKEN'], os.environ['A_TOKEN_SECRET'])
  api = tweepy.API(auth)

  api.update_with_media(file,text)
  # you should read the img directory and delete file after posting
  
def tweet_image():
    url = 'http://qnimate.com/wp-content/uploads/2014/03/images2.jpg'
    response = requests.get(url, stream=True)
     #you shold be able to specify a path, check glitch support for writing to ASSETS or to .tmp folder
    with open('img.jpg', 'wb') as out_file:
      shutil.copyfileobj(response.raw, out_file)
      from PIL import Image, ImageDraw, ImageFile
      ImageFile.LOAD_TRUNCATED_IMAGES = True

      im = Image.open("img.jpg")

      draw = ImageDraw.Draw(im)
      draw.rectangle((0, 0) + im.size, fill=128, 200)
      draw.line((0, im.size[1], im.size[0], 0), fill=(128, 128, 128))
      del draw

# write to stdout
      im.save('img.jpg')
      del response
    filename = 'img.jpg'
    text = "no!"
    
    return filename,text

if __name__ == "__main__":
  image,text = tweet_image()
  tweet(image,text)
  