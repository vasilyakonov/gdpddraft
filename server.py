import requests
import os
import tweepy


def twitter_api():
    auth = tweepy.OAuthHandler(os.environ['C_KEY'], os.environ['C_SECRET'])
    auth.set_access_token(os.environ['A_TOKEN'], os.environ['A_TOKEN_SECRET'])
    api = API(auth)
    return api


def tweet_image(url, message):
    api = tweepy.API(auth)
    filename = 'e813cbb64ced5d7d8cc24a0789720729.jpg'
    request = assets.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unable to download image")


url = "https://cdn.glitch.com/c8f6cb80-020b-4743-b6ab-6e2bd79b5782%2Fe813cbb64ced5d7d8cc24a0789720729.jpg?1519725876589"
message = "Nice one"
tweet_image(url, message)