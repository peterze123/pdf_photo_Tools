import sys
import os
from PIL import Image

arg1 = sys.argv[1]
arg2 = sys.argv[2]
current = './tester/'
path = os.path.join(current, arg1, arg2)
# create a new path
try:
    os.mkdir(path)
except FileExistsError:
    pass
pokedex = os.path.join(current, arg1)
# converts and stores the files
for i in os.listdir(pokedex):
    try:
        if i.endswith('.jpg'):
            img = Image.open(os.path.join(pokedex, i))
            img.save(path + i[:-3] + 'png') #other forms
    except FileExistsError:
        continue
        
