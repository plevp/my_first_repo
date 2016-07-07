# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

import os
import sys
import wget



def main(url):
    os.chdir("all_examples")
    #url = raw_input('Enter - ')

    doit(url)

def doit(url):
    print "URL:", url
    html = urllib.urlopen(url).read()

    soup = BeautifulSoup(html)
    
    # Retrieve all of the anchor tags
    tags = soup('a')
    
    suffixes = {}
    for tag in tags:
        # Look at the parts of a tag
    
        url_ = tag.get('href', None)
    
        #print 'TAG:',tag
        #print 'URL:',tag.get('href', None)
        #print 'Contents:',tag.contents[0]
        #print 'Attrs:',tag.attrs

        l = url_.split('.')
        if len(l) > 1:
            suff = l[-1]
        else:
            print 'TAG:',tag
            print 'URL:',tag.get('href', None)
            print 'Contents:',tag.contents[0]
            print 'Attrs:',tag.attrs
            if url_[0] == '?' or url_[0] == '/':
                continue
            else:
                suff = "None"
        if suff not in suffixes:
            suffixes[suff] = []
        suffixes[suff].append(url_)

    print suffixes

    for (k,v) in suffixes.items():
        if k != "None":
            for i in v:
                p = url + "/" + i
                filename = wget.download(p)

                print "   ", filename
        else:
            for i in v:
                os.mkdir(i)
                os.chdir(i)
                doit(url + "/" + i)
                os.chdir("..")
            
        
main("http://www.pythonlearn.com/code")
