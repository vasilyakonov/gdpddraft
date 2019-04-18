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
import uuid

u = uuid.uuid1()


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


#gradients_response = open('gradients.json').read()
#the_gradients = json.loads(gradients_response)
coldgradients_list = ["Aqua",
                      "Cyan",
                      "PaleTurquoise",
                      "Aquamarine",
                      "Turquoise",
                      "LightSteelBlue",
                      "LightBlue",
                      "PowderBlue",
                      "SkyBlue",
                      "LightSkyBlue",
                      "DeepSkyBlue",
                      "DodgerBlue",
                      "CornflowerBlue",
                      "Lavender",
                      "Alice Blue"]

warmgradients_list = ["Pink",
                      "HotPink",
                     "DeepPink",
                     "MediumVioletRed",
                     "LightSalmon",
                     "Salmon",
                     "LightCoral",
                     "IndianRed",
                     "Crimson",
                     "Firebrick",
                     "DarkRed",
                     "Red",
                     "OrangeRed",
                     "Tomato",
                     "Coral",
                     "DarkOrange",
                     "Orange",
                     "SandyBrown",
                     "Brown",
                     "Maroon"]
                  

middlegradients_list = ["Gainsboro",
                       "LightGray",
                       "WhiteSmoke",
                        "GhostWhite",
                        "Mint Cream"]

warmergradients_list = ["PapayaWhip",
                       "Moccasin",
                       "PeachPuff",
                       "Cornsilk",
                       "BlanchedAlmond",
                       "Bisque",
                        "LavenderBlush",
                     "MistyRose",
                        "Seashell",
                        "Snow"
                       ]

coldgradient = '%s' % (random.choice(tuple(coldgradients_list)))
warmgradient = '%s' % (random.choice(tuple(warmgradients_list)))
middlegradient = '%s' % (random.choice(tuple(middlegradients_list)))
warmergradient = '%s' % (random.choice(tuple(warmergradients_list)))


"""for f in the_gradients:
   gradients_list.append(f)
print len(gradients_list)"""


# load the file
with open("./docs/index.html") as inf:
    txt = inf.read()
    soup = bs4.BeautifulSoup(txt, features="html.parser")
    print(soup.prettify())


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

soup.style.string =""

#gradient ='%s' % (random.choice(tuple(gradients_list)))
soup.style.append("body{background-image: linear-gradient(%s, %s, %s, %s);}" % (coldgradient, middlegradient, warmergradient, warmgradient))


# save the file again
with open("./docs/index.html", "w") as outf:
    outf.write(str(soup.prettify(formatter=None)))
    print(soup.prettify())
    


#from flask import Flask

#from flask import Flask, render_template

#app = Flask(__name__)

#@app.route('/')
#def index():
     #return render_template('index.html')
  
#@app.route('/calendar')
#def calendar():
    # return render_template('calendar.html')
  
#@app.route('/typefaces')
#def typefaces():
     #return render_template('typefaces.html')
  
#@app.route('/lugemik')
#def lugemik():
     #return render_template('lugemik.html')
  
#@app.route('/imposter')
#def imposter():
     #return render_template('imposter.html')

#@app.route('/hypergraphx')
#def hypergraphx():
     #return render_template('hypergraphx.html')
  
#@app.route('/riding')
#def riding():
    # return render_template('riding.html')

#@app.route('/interview')
#def interview():
     #return render_template('interview.html')
  
#@app.route('/digest')
#def digest():
    # return render_template('digest.html')
  
#@app.route('/tools')
#def tools():
     #return render_template('tools.html')
  
#@app.route('/cposter')
#def cposter():
   #  return render_template('cposter.html')
  
#if __name__ == '__main__':
 #   app.run(debug=False)
    
    
#subprocess.call("refresh")
u = uuid.uuid1()
#subprocess.call('git commit -a -m "%s"' % uuid.uuid1())
process = subprocess.Popen(["git", "commit", "-a", "-m'%s'" % uuid.uuid1()], stdout=subprocess.PIPE)
output = process.communicate()[0]
output = subprocess.check_output(["git", "push"])