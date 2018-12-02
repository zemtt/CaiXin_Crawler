# -*- coding:utf-8 -*-

import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

null = None

url = "http://tag.caixin.com/news/homeInterface.jsp?channel={}&start={}&count={}&picdim={}&callback={}&_={}"

data = {}
data['channel'] = '125'
data['start'] = 0
data['count'] = 100
data['picdim'] = '_145_97'
data['callback'] = 'jQuery17201966897926415454_1543651030411'
data['_'] = '1543651030411'

linksList = []

def feedUrl(url, data):
    return url.format(
        data['channel'],
        data['start'],
        data['count'],
        data['picdim'],
        data['callback'],
        data['_']
    )

for i in range(10):
    data['start'] = i
    a = feedUrl(url,data)
    returnInfo = json.loads(requests.get(a).text.strip()[41:-2])
    linksList.append(returnInfo['datas'])
    print u'第{}页抓取完毕。'.format(i+1)
    #time.sleep(10)

with open('test.json','w') as f:
    json.dump(linksList, f, ensure_ascii=False)