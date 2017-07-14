#!/usr/bin/python

print "Content-type:application/json"
print "Access-Control-Allow-Origin: *\r\n\r\n"


import sys
# do this to in case you have to call the script from symlink 
sys.path.insert(0, '/Users/joshua/dev/python/first')

import cgi
import json
import random
import sys
import time
import mydb

#FUNCTION DEFINITIONS #############
def getData(req):
    action = req['action']
    data={}
    if (action=="load.chapter"):
        book = req['book']
        chapter=req['chapter']
        verses=mydb.getWholeChapter(book,chapter)
        data={"verses":verses}
    else:
        data={} 

    return data

#FUNCTION DEFINITIONS #############

now = time.localtime()
rand = random.randint(0,500)

resp = {
    "error":"",
    'date' : time.strftime("%b %d %Y %H:%M:%S",now)
    }
try:
    req = json.load(sys.stdin)

    #start processing data
    resp['req']=req
    resp['data'] = getData(req)
except:
    resp["error"]="Invalid/No Post data Found"
    verses=mydb.getWholeChapter(1,1)
    data={"verses":verses}
    resp['data'] = data


print(json.dumps(resp))

# call ends here, no futher dialogue

        
