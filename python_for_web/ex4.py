import urllib
import xml.etree.ElementTree as ET

#url ='http://python-data.dr-chuck.net/comments_223890.xml'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = urllib.urlopen(address)
    data = url.read()

    tree = ET.fromstring(data)

    sum = 0
    results = tree.findall('comments')[0].findall('comment');
    for x in results:
        sum += int(x.findall('count')[0].text)
    
    print sum

    
