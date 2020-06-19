#!/usr/bin/env python3
import os
from PIL import Image
# Open a file
path = "/home/"+os.environ.get('USER')+"/supplier-data/images/"
dirs = os.listdir( path)
for infile in dirs:
       f=os.path.splitext(infile)[0]
       outfile =path+f
       try:
          with Image.open(path+infile) as im:
                 if im.format=='TIFF':
                    im = im.convert("RGB")
                    im.resize((600,400)).save(outfile+".jpeg")
       except:
          pass


