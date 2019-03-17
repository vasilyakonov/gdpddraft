# -*- coding: utf-8 -*-
from git import Repo

repo_dir = 'templates'
repo = Repo(repo_dir, search_parent_directories=True)
file_list = [
    'templates/cool-file.html'
]
commit_message = 'Add simple regression analysis'
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()

info = origin.push()[0]
print(info.summary)