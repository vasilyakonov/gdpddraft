import requests
import os
import tweepy


def create tweet():
   filename = 'e813cbb64ced5d7d8cc24a0789720729.jpg'
  
   the_image = request.get(filename)


#def tweet_image(url, message):
 #   api = tweepy.API()
  #  filename = 'e813cbb64ced5d7d8cc24a0789720729.jpg'
  #  request = request.get(filename, stream=True)
   # if request.status_code == 200:
   #     with open(filename, 'wb') as image:
     #       for chunk in request:
        #        image.write(chunk)

      #  api.update_with_media(filename, status=message)
      #  os.remove(filename)
    #else:
       # print("Unable to download image")
      
def tweet(text):
  """Send out the text as a tweet."""
  # Twitter authentication
  auth = tweepy.OAuthHandler(os.environ['C_KEY'], os.environ['C_SECRET'])
  auth.set_access_token(os.environ['A_TOKEN'], os.environ['A_TOKEN_SECRET'])
  api = tweepy.API(auth)

  # Send the tweet and log success or failure
  # try:
  api.update_with_media(filename)
  os.remove(filename)
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
  