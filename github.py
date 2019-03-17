# -*- coding: utf-8 -*-
from git import Repo

repo_dir = 'templates'
repo = Repo(repo_dir)
file_list = [
    'templates/hypergraphx.html',
    'templates/index.html'
]
commit_message = 'Add simple regression analysis'
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('https://github.com/vasilyakonov/GDPD-Draft.git')
origin.push()