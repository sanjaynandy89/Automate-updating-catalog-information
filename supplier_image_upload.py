#!/usr/bin/env python3
import os
import requests
path = "/home/"+os.environ.get('USER')+"/supplier-data/images/"
dirs = os.listdir( path)
list=[]
for infile in dirs:
       f=os.path.splitext(infile)[0]
       e=os.path.splitext(infile)[1]
       print(infile)
       if e=='.jpeg':
          list.append(infile)
print(list)
# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://34.71.201.30/upload/"
for f in list:
   with open(path+f, 'rb') as opened:
         r = requests.post(url, files={'file': opened})

