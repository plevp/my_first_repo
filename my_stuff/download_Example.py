import urllib2
import sys
import os
import BeautifulSoup
from subprocess import call

try:
    url = "http://web.eecs.umich.edu/~radev/coursera-slides"
    s = urllib2.urlopen(url)
    soup = BeautifulSoup.BeautifulSoup(s)
    print soup.prettify();
    ass = soup.findAll("a")
    print len(ass)
    for item in ass:
	print item.text
	print url+ "/"+ item['href']
	call(["wget", "-P", "all_slides", url+"/"+ item['href']])
	     
except:
    print "Error in connection. Please check URL again. "



## http://web.eecs.umich.edu/~radev/coursera-slides/
