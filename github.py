# -*- coding: utf-8 -*-
from git import Repo

repo_dir = 'templates'
repo = Repo(repo_dir, search_parent_directories=True)
file_list = [
    'templates/hypergraphx.html',
    'templates/index.html'
]
commit_message = 'Add simple regression analysis'
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()
print(origin.push())