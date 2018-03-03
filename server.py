# -*- coding: utf-8 -*-

import requests
import os
import tweepy
import shutil
import PIL
import pip
import aggdraw
import urllib
import json
import random





def tweet(file,text):
  """Send out the text as a tweet."""
  # Twitter authentication
  auth = tweepy.OAuthHandler(os.environ['C_KEY'], os.environ['C_SECRET'])
  auth.set_access_token(os.environ['A_TOKEN'], os.environ['A_TOKEN_SECRET'])
  api = tweepy.API(auth)

  api.update_with_media(file,text)
  # you should read the img directory and delete file after posting
  
def tweet_image():
  
    images_response = requests.get('https://botwiki.org/corpora-api/')
    the_images = images_response.json()
    images_list = []
  
    for f in the_images["isms"]:
      for k, v in f.iteritems():
        images_list.append(v)

    n = random.randint(0,len(images_list))
    the_image = images_list[n]

    url = '%s' % (the_image)
    response = requests.get(url, stream=True)
     #you shold be able to specify a path, check glitch support for writing to ASSETS or to .tmp folder
    with open('img.jpg', 'wb') as out_file:
      shutil.copyfileobj(response.raw, out_file)
      from PIL import Image, ImageDraw, ImageFile
      ImageFile.LOAD_TRUNCATED_IMAGES = True

      im = Image.open("img.jpg")
      
      
      
      
      url2 = 'https://cdn.glitch.com/c8f6cb80-020b-4743-b6ab-6e2bd79b5782%2FArchivo-Regular.ttf?1520096937377'
    response = requests.get(url2, stream=True)
     #you shold be able to specify a path, check glitch support for writing to ASSETS or to .tmp folder
    with open('font.ttf', 'wb') as out_file:
      shutil.copyfileobj(response.raw, out_file)
      
      municipalities_response = requests.get('https://botwiki.org/api/corpora/data/geography/canadian_municipalities.json')
      the_municipalities = municipalities_response.json()
      municipalities_list = []
  
      for f in the_municipalities["municipalities"]:
        for k, v in f.iteritems():
          municipalities_list.append(v)

      n = random.randint(0,len(municipalities_list))
      the_municipality = municipalities_list[n]

      plant_response = requests.get('https://botwiki.org/api/corpora/data/plants/plants.json')
      the_plants = plant_response.json()
      plant_list = []

      for p in the_plants['instruments']:
        plant_list.append(p['name'])

      m = random.randint(0,len(plant_list))
      the_plant = plant_list[m]

  #the_tweet = "A %s samiyam %s commencement %s" % (the_municipality,the_plant)
      
      
      
      

      font = aggdraw.Font((255, 255, 255), "/app/font.ttf")
      d = aggdraw.Draw(im)
      p = aggdraw.Pen((255, 255, 255), 100)
      b = aggdraw.Brush((255, 255, 255))
      #d.ellipse((0, 0, 500, 500), p, b)
      #d.ellipse((0, 500, 500, 0), p, b)
      d.text((100, 100), "suck on my %s , you %s " % (the_municipality,the_plant), font)
      d.flush()
      del d

# write to stdout
      im.save('/app/img.jpg')
      del response
    filename = 'img.jpg'
    text = "no!"
    
    return filename,text

if __name__ == "__main__":
  image,text = tweet_image()
  tweet(image,text)
  