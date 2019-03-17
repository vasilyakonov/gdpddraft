# -*- coding: utf-8 -*-
from git import Repo

repo_dir = 'templates'
repo = Repo(repo_dir, search_parent_directories=True)
file_list = [
  'templates/calendar.html',
'templates/cool-file.html',
'templates/cposter.html',
'templates/digest.html',
'templates/hypergraphx.html',
'templates/imposter.html',
'templates/index.html',
'templates/interview.html',
'templates/layout.html',
'templates/lugemik.html',
'templates/riding.html',
'templates/tools.html',
'templates/typefaces.html',
  'templates/README.md'
]
commit_message = 'Add simple regression analysis'
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()

info = origin.push()[0]
print(info.summary)