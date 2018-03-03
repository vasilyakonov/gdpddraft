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
import dropbox


# Get your app key and secret from the Dropbox developer website
app_key = os.environ['A_KEY2']
app_secret = os.environ['A_SECRET2']

flow = dropbox.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

# Have the user sign in and authorize this token
authorize_url = flow.start()
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'
code = raw_input("Enter the authorization code here: ").strip()

# This will fail if the user enters an invalid authorization code
access_token, user_id = flow.finish(code)

client = dropbox.DropboxClient(os.environ['A_TOKEN2'])
print 'linked account: ', client.account_info()

f = open('working-draft.txt', 'rb')
response = client.put_file('/magnum-opus.txt', f)
print 'uploaded: ', response

folder_metadata = client.metadata('/')
print 'metadata: ', folder_metadata

f, metadata = client.get_file_and_metadata('/magnum-opus.txt')
out = open('magnum-opus.txt', 'wb')
out.write(f.read())
out.close()
print metadata



