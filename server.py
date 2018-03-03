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


dbx = dropbox.Dropbox(os.environ['A_TOKEN2'])
dbx.users_get_current_account()
dbx.files_download('/Cavs vs Warriors/Game 5/cool-file.json')
#print(dbx.files_get_metadata('/KIng of Carrot Flowers Pt2/cool-file.json').server_modified)
