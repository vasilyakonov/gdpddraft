# -*- coding: utf-8 -*-

import os
import requests
import random
import flask
import shutil
import bs4
import jinja2
import subprocess
import json

from bs4 import BeautifulSoup 


"""markup = <div class="object_one"> <h1>Journal For Raw Visual Data</h1> 
      Praesent efficitur, nibh vitae fringilla scelerisque, est neque faucibus quam, in iaculis purus libero eget mauris. Curabitur et luctus sapien, ac gravida orci. Aliquam erat volutpat. In hac habitasse platea dictumst. Aenean commodo, arcu a commodo efficitur, libero dolor mollis turpis, non posuere orci leo eget enim. Curabitur sit amet elementum orci, pulvinar dignissim urna. Morbi id ex eu ex congue laoreet. Aenean tincidunt dolor justo, semper pretium libero luctus nec. Ut vulputate metus accumsan leo imperdiet tincidunt. Phasellus nec rutrum dolor. Cras imperdiet sollicitudin arcu, id interdum nibh fermentum in.
    </div>
<div class="object_two"> <h1>Imposter</h1> 
      Praesent efficitur, nibh vitae fringilla scelerisque, est neque faucibus quam, in iaculis purus libero eget mauris. Curabitur et luctus sapien, ac gravida orci. Aliquam erat volutpat. In hac habitasse platea dictumst. Aenean commodo, arcu a commodo efficitur, libero dolor mollis turpis, non posuere orci leo eget enim. Curabitur sit amet elementum orci, pulvinar dignissim urna. Morbi id ex eu ex congue laoreet. Aenean tincidunt dolor justo, semper pretium libero luctus nec. Ut vulputate metus accumsan leo imperdiet tincidunt. Phasellus nec rutrum dolor. Cras imperdiet sollicitudin arcu, id interdum nibh fermentum in.
    </div>
<div class="object_three"> <h1>Interview Magazine</h1> 
      Praesent efficitur, nibh vitae fringilla scelerisque, est neque faucibus quam, in iaculis purus libero eget mauris. Curabitur et luctus sapien, ac gravida orci. Aliquam erat volutpat. In hac habitasse platea dictumst. Aenean commodo, arcu a commodo efficitur, libero dolor mollis turpis, non posuere orci leo eget enim. Curabitur sit amet elementum orci, pulvinar dignissim urna. Morbi id ex eu ex congue laoreet. Aenean tincidunt dolor justo, semper pretium libero luctus nec. Ut vulputate metus accumsan leo imperdiet tincidunt. Phasellus nec rutrum dolor. Cras imperdiet sollicitudin arcu, id interdum nibh fermentum in.
    </div>
<div class="object_four"> <h1>Critical Poster</h1> 
      Praesent efficitur, nibh vitae fringilla scelerisque, est neque faucibus quam, in iaculis purus libero eget mauris. Curabitur et luctus sapien, ac gravida orci. Aliquam erat volutpat. In hac habitasse platea dictumst. Aenean commodo, arcu a commodo efficitur, libero dolor mollis turpis, non posuere orci leo eget enim. Curabitur sit amet elementum orci, pulvinar dignissim urna. Morbi id ex eu ex congue laoreet. Aenean tincidunt dolor justo, semper pretium libero luctus nec. Ut vulputate metus accumsan leo imperdiet tincidunt. Phasellus nec rutrum dolor. Cras imperdiet sollicitudin arcu, id interdum nibh fermentum in.
    </div>
<div class="object_five"> <h1>Calendar</h1> 
      Praesent efficitur, nibh vitae fringilla scelerisque, est neque faucibus quam, in iaculis purus libero eget mauris. Curabitur et luctus sapien, ac gravida orci. Aliquam erat volutpat. In hac habitasse platea dictumst. Aenean commodo, arcu a commodo efficitur, libero dolor mollis turpis, non posuere orci leo eget enim. Curabitur sit amet elementum orci, pulvinar dignissim urna. Morbi id ex eu ex congue laoreet. Aenean tincidunt dolor justo, semper pretium libero luctus nec. Ut vulputate metus accumsan leo imperdiet tincidunt. Phasellus nec rutrum dolor. Cras imperdiet sollicitudin arcu, id interdum nibh fermentum in.
    </div>
<div class="object_six"> <h1>WYSIWYG</h1> 
      Praesent efficitur, nibh vitae fringilla scelerisque, est neque faucibus quam, in iaculis purus libero eget mauris. Curabitur et luctus sapien, ac gravida orci. Aliquam erat volutpat. In hac habitasse platea dictumst. Aenean commodo, arcu a commodo efficitur, libero dolor mollis turpis, non posuere orci leo eget enim. Curabitur sit amet elementum orci, pulvinar dignissim urna. Morbi id ex eu ex congue laoreet. Aenean tincidunt dolor justo, semper pretium libero luctus nec. Ut vulputate metus accumsan leo imperdiet tincidunt. Phasellus nec rutrum dolor. Cras imperdiet sollicitudin arcu, id interdum nibh fermentum in.
    </div>
<div class="object_seven"> <h1>Digital Unconscious</h1> 
      Praesent efficitur, nibh vitae fringilla scelerisque, est neque faucibus quam, in iaculis purus libero eget mauris. Curabitur et luctus sapien, ac gravida orci. Aliquam erat volutpat. In hac habitasse platea dictumst. Aenean commodo, arcu a commodo efficitur, libero dolor mollis turpis, non posuere orci leo eget enim. Curabitur sit amet elementum orci, pulvinar dignissim urna. Morbi id ex eu ex congue laoreet. Aenean tincidunt dolor justo, semper pretium libero luctus nec. Ut vulputate metus accumsan leo imperdiet tincidunt. Phasellus nec rutrum dolor. Cras imperdiet sollicitudin arcu, id interdum nibh fermentum in.
    </div>
<div class="object_eight"> <h1>Typefaces</h1> 
      Praesent efficitur, nibh vitae fringilla scelerisque, est neque faucibus quam, in iaculis purus libero eget mauris. Curabitur et luctus sapien, ac gravida orci. Aliquam erat volutpat. In hac habitasse platea dictumst. Aenean commodo, arcu a commodo efficitur, libero dolor mollis turpis, non posuere orci leo eget enim. Curabitur sit amet elementum orci, pulvinar dignissim urna. Morbi id ex eu ex congue laoreet. Aenean tincidunt dolor justo, semper pretium libero luctus nec. Ut vulputate metus accumsan leo imperdiet tincidunt. Phasellus nec rutrum dolor. Cras imperdiet sollicitudin arcu, id interdum nibh fermentum in.
    </div>"""

entries_response = open('entries.json').read()
the_entries = json.loads(entries_response)
entries_list = []


for f in the_entries:
   entries_list.append(f)
print len(entries_list)


gradient_response = open('gradients.json').read()
the_gradients = json.loads(gradients_response)
gradients_list = []


for f in the_gradients:
   gradients_list.append(f)
print len(gradients_list)


# load the file
with open("./templates/index.html") as inf:
    txt = inf.read()
    soup = bs4.BeautifulSoup(txt, features="html.parser")
    print(soup.prettify())

# create new link
#new_link = soup.new_tag("link", rel="icon", type="image/png", href="img/tor.png")
# insert it into the document
soup.main.string =""

object1 = '%s' % (random.choice(tuple(entries_list)))

soup.main.append(object1)
entries_list.remove(object1)

object2 = '%s' % (random.choice(tuple(entries_list)))

soup.main.append(object2)
entries_list.remove(object2)

object3 = '%s' % (random.choice(tuple(entries_list)))

soup.main.append(object3)
entries_list.remove(object3)

object4 = '%s' % (random.choice(tuple(entries_list)))

soup.main.append(object4)
entries_list.remove(object4)

object5 = '%s' % (random.choice(tuple(entries_list)))

soup.main.append(object5)
entries_list.remove(object5)

object6 = '%s' % (random.choice(tuple(entries_list)))

soup.main.append(object6)
entries_list.remove(object6)

object7 = '%s' % (random.choice(tuple(entries_list)))

soup.main.append(object7)
entries_list.remove(object7)

object8 = '%s' % (random.choice(tuple(entries_list)))

soup.main.append(object8)
entries_list.remove(object8)

object9 = '%s' % (random.choice(tuple(entries_list)))

soup.main.append(object9)
entries_list.remove(object9)

object10 = '%s' % (random.choice(tuple(entries_list)))

soup.main.append(object10)
entries_list.remove(object10)

object11 = '%s' % (random.choice(tuple(entries_list)))

soup.main.append(object11)
entries_list.remove(object11)

object12 = '%s' % (random.choice(tuple(entries_list)))

soup.main.append(object12)
entries_list.remove(object12)

gradient ='%s' % (random.choice(tuple(gradients_list)))
soup.style.append(gradient)



# save the file again
with open("./templates/index.html", "w") as outf:
    outf.write(str(soup.prettify(formatter=None)))
    print(soup.prettify())

    
