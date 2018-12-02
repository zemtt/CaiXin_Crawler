# -*- coding:utf-8 -*-

import requests
import json
from src.Date import Date
import sys, io
reload(sys)
sys.setdefaultencoding('utf-8') 

main_url = 'http://finance.caixin.com/'
date_1 = Date('2018-11-29')
date_2 = date_1 - 1
aid = 101353349

def getUrl(date, aid):
    return main_url + str(date) + '/' + str(aid) + '.html'


while 1:
    aid -= 1
    url_1 = getUrl(date_1, aid)
    url_2 = getUrl(date_2, aid)
    sign = '您要访问的页面不存在或已被移除！'
    f1 = sign in requests.get(url_1).text
    f2 = sign in requests.get(url_2).text
    if f1:
        print url_1 + u'   [ERROR]'
    else:
        with open('links', 'a+') as f:
            f.write(url_1+'\n')
        print url_1 + u'   [OK]'

    if f2:
        print url_2 + u'   [ERROR]'
    else:
        with open('links', 'a+') as f:
            f.write(url_2+'\n')
        print url_2 + u'   [OK]'
        date_1 -= 1
        date_2 -= 1
    print