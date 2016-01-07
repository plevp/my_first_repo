import xml.etree.ElementTree as ET

data = '''
<abc>
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>

<person>
  <name>Chuck2</name>
  <phone type="intl">
     +1 734 303 4457
   </phone>
   <email hide="yes"/>
</person>
</abc>
'''

tree = ET.fromstring(data)


for child in tree:
    print 'Attr:',child.find('name').text
    print 'Attr:',child.find('email').get('hide')
    

