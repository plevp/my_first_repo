from bs4 import BeautifulSoup
import urllib2
import webbrowser

print 'enter=next article, y=open artcle, x=exit'
print '-------------------------------------------'
while True:
    content=urllib2.urlopen('http://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=xml')
    xml=content.read()
    content.close()
    soup=BeautifulSoup(xml)
    links=soup.findAll('page')
    for l in links:
        choice=raw_input('Would you like to read about '+l.get('title').encode('ascii', 'ignore')+'?')
        if choice=='yes':
            webbrowser.open_new_tab('http://en.wikipedia.org/wiki?curid='+l.get('id'))
        elif choice=='x':
            exit(0)
