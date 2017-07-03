#!/usr/bin/env python

import urllib2

response = None

try:
    response = urllib2.urlopen('http://localhost:18080/')
except urllib2.URLError as e:
    print (e.reason)

if response.code == 200:
    print "We got an HTML response!"
    print (response.read())
else:
    print ("Something went wrong!")


