# -*- coding: utf-8 -*-
import bs4
import shutil
import os
import subprocess


from bs4 import BeautifulSoup 

markup ="""<div class="object_one"> <h1>Journal For Raw Visual Data</h1> 
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

# load the file
with open("./templates/index.html") as inf:
    txt = inf.read()
    soup = bs4.BeautifulSoup(txt, features="html.parser")
    print(soup.prettify())

# create new link
new_link = soup.new_tag("link", rel="icon", type="image/png", href="img/tor.png")
# insert it into the document
soup.body.append(markup)

# save the file again
with open("./templates/index.html", "w") as outf:
    outf.write(str(soup.prettify(formatter=None)))
    print(soup.prettify())

subprocess.call("refresh")    