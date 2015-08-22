import urllib2
import json
import pandas as pd

courses_response = urllib2.urlopen('https://api.coursera.org/api/catalog.v1/courses?fields=shortName,name,language&includes=universities,categories')
courses_data = json.load(courses_response)
courses_data = courses_data['elements']

categories_response = urllib2.urlopen('https://api.coursera.org/api/catalog.v1/categories')
categories_data = json.load(categories_response)
categories_data = categories_data['elements']

categories = [(c['id'], c['name']) for c in categories_data]
categories.sort()

print categories()

courses_df = pd.DataFrame()

courses_df['course_name'] = map(lambda course_data: course_data['name'], courses_data)
courses_df['course_language'] = map(lambda course_data: course_data['language'], courses_data)
courses_df['course_short_name'] = map(lambda course_data: course_data['shortName'], courses_data)
courses_df['categories'] = map(lambda course_data: course_data['links']['categories'] if 'categories' in course_data['links'] else [], courses_data)
courses_df['universities'] = map(lambda course_data: course_data['links']['universities'] if 'universities' in course_data['links'] else [], courses_data)

sessions_response = urllib2.urlopen("https://api.coursera.org/api/catalog.v1/sessions?fields=courseId,startDay,startMonth,startYear,status,durationString")
sessions_data = json.load(sessions_response)
sd = sessions_data['elements']

sd3 = filter(lambda x: 'startYear' in x and x['startYear']  == 2015 and (x['startMonth'] == 8 or x['startMonth'] == 9), sd)


def findcourse(courseid):
    t = filter(lambda x : x['id'] == courseid, courses_data) 
    return {} if len(t) == 0 else t[0]




temp = map(lambda x: (x.startMonth, x. startDay, findcourse(ex.courseId)['name']), sd3)


temp = map(lambda x: (x['startMonth'], '?' if 'startDay' not in x else x['startDay'], findcourse(x['courseId'])['name']), sd3)

temp2 = filter(lambda x: x[1] != '?', temp)

temp3 = sorted(temp2, key = lambda x: (x[0], x[1]))

