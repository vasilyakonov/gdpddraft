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
dbx.files_download("cool-file.json, rev=None)

