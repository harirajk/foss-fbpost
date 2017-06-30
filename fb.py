import json
import os
import numpy

topic=input("Post to be entered")
topic=topic.lower()
a={}
with open('fbposts.json') as f:
	posts=json.load(f)
	for a in posts:
		for key,value in a.iteritems():
            if value.lower()==topic:
     		   print("Topic already posted")
     		   print a
	    	   break
		    else:
			   print("Topic not added")
