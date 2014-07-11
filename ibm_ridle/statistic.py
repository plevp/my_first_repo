#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ibi ridle pages statistics
"""
import BeautifulSoup
import sys, os 
import urllib, urllib2 

ALL_USERS = {} # for dictionnary to check all users users 

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

years = ["2013", "2014"]

baseurl = "http://domino.research.ibm.com/Comm/wwwr_ponder.nsf/Challenges/"

def do_one(year, month):
    
    url = baseurl + month + year + ".html"
    print url
    try:
        soup = BeautifulSoup.BeautifulSoup(urllib2.urlopen(url))
    except:
        return None

    #pr = soup.prettify()
    #print pr

    bs = soup.findAll("b")
    
    n = ''
    names = []
    item =  bs[0]
    while (item):
        if item.string == None:
            if item.name == 'b':
                if item.text != '*':
                    n = n + item.text
            elif item.name == 'br':
                if n[0] == '*':
                    n = n[1:]
                if n.find("&amp;") >= 0:
                    n = n.replace("&amp;", '&')
                names.append(n)
                n = ''

        item = item.nextSibling                

    #print "Answers: ", len(names)
    return names

def doit():
    #count = 0
    res = []
    d = False
    for y in years:
        for m in months:
            l = do_one(y, m)
            if l == None:
                d = True
                break
            #print y, m
            #print l
            if "Anatoli Plotnikov" in l:
                #count += 1
                res.append((m, y, l.index("Anatoli Plotnikov"), len(l)))

            llen = len(l)
            for u in l:
                if ALL_USERS.get(u) == None:
                    ALL_USERS[u] = []
                ALL_USERS[u].append((m, y, l.index(u), llen))
        if d:
            break
    #print count
    print res

    #print ALL_USERS

    l1 = map(lambda (key, value): (key, len(value)), ALL_USERS.iteritems())

    l2 = sorted(l1, key = lambda (k, v) : v , reverse = True)

    for (k, dummy_v) in  l2[0:100]:
        print "\n*****User: ", k
        print ALL_USERS[k]

    print "User number: ", len(ALL_USERS)

    print ALL_USERS["Anatoli Plotnikov"]
    
if __name__ == '__main__':
    doit()

'''
'soup'
'type(soup)'
'dir(soup)'
'soup.text()'
'soup.find("Plotnikov")'
'a = soup.find("Plotnikov")'
'print a'
'a = soup.getText()'
'print a'
'history'
'soup.prettyPrint()'
'soup.prettyfy()'
'p = soup.prettify()'
'print p'
'p1 = str(p)'
'print p1'
'peinr p'
'print p'
'f1 = open("ibm_ridle", w)'
'f1 = open("ibm_ridle", "w")'
'f1.write(p)'
'f1.close()'
'readline.get_history_items()'
'import readline'
'readline.get_history_items()'
'readline.get_history_item()'
'for i in range(readline.get_current_history_length()):'
'readline.get_history_item(i)'
'for i in range(readline.get_current_history_length()):'
'''
