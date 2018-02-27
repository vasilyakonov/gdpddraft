import requests
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
    filename = 'https://raw.githubusercontent.com/openimages/dataset/master/assets/oid_bbox_examples.png'
    text = "Hello!"
    
    return filename,text

if __name__ == "__main__":
  image,text = tweet_image()
  tweet(image,text)
  