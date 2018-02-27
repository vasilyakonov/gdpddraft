import requests
import os
import tweepy


def tweet_image(url, message):
    url = "https://cdn.glitch.com/c8f6cb80-020b-4743-b6ab-6e2bd79b5782%2Fe813cbb64ced5d7d8cc24a0789720729.jpg?1519725876589"
    api = tweepy.API()
    filename = 'e813cbb64ced5d7d8cc24a0789720729.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename)
        os.remove(filename)
    else:
        print("Unable to download image")
        
    return the_tweet


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



#url = "https://cdn.glitch.com/c8f6cb80-020b-4743-b6ab-6e2bd79b5782%2Fe813cbb64ced5d7d8cc24a0789720729.jpg?1519725876589"
#message = "Nice one"
#tweet_image(url, message)
url = "https://cdn.glitch.com/c8f6cb80-020b-4743-b6ab-6e2bd79b5782%2Fe813cbb64ced5d7d8cc24a0789720729.jpg?1519725876589"
message = "1"
if __name__ == "__main__":
  tweet_image = tweet_image(url,message)
  tweet(tweet_image)
  