#!/usr/bin/python

import os
import sys
import cgi, cgitb


# do this to in case you have to call the script from symlink 
sys.path.insert(0, '/Users/joshua/dev/python/first')

form = cgi.FieldStorage()

source = form.getvalue('source')
fname = form.getvalue('fname')

FILE_NAME="/Users/joshua/dev/python/pi/hellopi.py"

if source == "code1":
    FILE_NAME="/Users/joshua/dev/uploads/"+source

elif source == "pi1":
    FILE_NAME="/Users/joshua/dev/python/pi/"+fname

#baseName = os.path.basename(FILE_NAME)
baseName= "source"

#print baseName

# HTTP Header
print('Content-Type:application/octet-stream; name="%s"\r\n'%(baseName))
print('Content-Disposition: attachment; filename="%s"\r\n'%(baseName))

buf = bytearray(os.path.getsize(FILE_NAME))
fo = open(FILE_NAME, 'rb')
fo.readinto(buf)

print(buf)

"""
import urllib2
FILE_NAME="http://localhost/cg.pdf"
response = urllib2.urlopen(FILE_NAME)
baseName='josh'
print('Content-Type:application/octet-stream; name="%s"\r\n'%(baseName))
print('Content-Disposition: attachment; filename="%s"\r\n\n'%(baseName))
"""

html = response.read()

