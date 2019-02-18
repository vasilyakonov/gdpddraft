# -*- coding: utf-8 -*-
import bs4
import shutil
import os


from bs4 import BeautifulSoup 

# load the file
with open("./templates/index.html") as inf:
    txt = inf.read()
    soup = bs4.BeautifulSoup(txt, features="html.parser")
    print(soup.prettify())

# create new link
new_link = soup.new_tag("link", rel="icon", type="image/png", href="img/tor.png")
# insert it into the document
soup.head.append(new_link)

# save the file again
with open("./templates/index.html", "w") as outf:
    outf.write(str(soup))
    print(soup.prettify())

    