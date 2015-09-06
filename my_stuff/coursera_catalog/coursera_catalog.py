import urllib2
import json
import pandas as pd

def findcourse(courseid, courses_data):
    t = filter(lambda x : x['id'] == courseid, courses_data) 
    return {} if len(t) == 0 else t[0]

def doit(year, m_from, m_to):

    courses_response = urllib2.urlopen('https://api.coursera.org/api/catalog.v1/courses?fields=shortName,name,language&includes=universities,categories')
    courses_data = json.load(courses_response)
    courses_data = courses_data['elements']

    categories_response = urllib2.urlopen('https://api.coursera.org/api/catalog.v1/categories')
    categories_data = json.load(categories_response)
    categories_data = categories_data['elements']

    sessions_response = urllib2.urlopen("https://api.coursera.org/api/catalog.v1/sessions?fields=courseId,startDay,startMonth,startYear,status,durationString")
    sessions_data = json.load(sessions_response)
    sd = sessions_data['elements']
    sd3 = filter(lambda x: 'startYear' in x and x['startYear']  == year and (x['startMonth'] >= m_from and x['startMonth'] <= m_to), sd)

    # temp = map(lambda x: (x.startMonth, x. startDay, findcourse(ex.courseId, courses_data)['name']), sd3)
    temp = map(lambda x: (x['startMonth'], '?' if 'startDay' not in x else x['startDay'], findcourse(x['courseId'], courses_data)['name']), sd3)
    temp2 = filter(lambda x: x[1] != '?', temp)
    temp3 = sorted(temp2, key = lambda x: (x[0], x[1]))
    return temp3


t = doit(2015, 9, 9)

for e in t:
    print e








