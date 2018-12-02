# -*- coding:utf-8 -*-

import io
import json
import sys
import thread
import time

import requests

from src.Date import Date

reload(sys)
sys.setdefaultencoding('utf-8')

LINK_FILE_PATH = 'links_0'
main_url = 'http://finance.caixin.com/'


def getLastLink():
    with open(LINK_FILE_PATH, 'r') as f:
        a = f.readlines()
    info = a[-1].split('/')[-2:]
    info[-1] = int(info[-1][:-6])
    return info


def getUrl(date, aid):
    return main_url + str(date) + '/' + str(aid) + '.html'


class Links_spider(object):
    def __init__(self, controller):
        self.date = Date()
        self.num = 0
        self.ct = controller

    def run(self):
        while 1:
            self.get_info()
            url_1 = getUrl(self.date, self.num)
            url_2 = getUrl(self.date-1, self.num)
            sign = '您要访问的页面不存在或已被移除！'
            f1 = sign in requests.get(url_1).text
            f2 = sign in requests.get(url_2).text
            # print f1, url_1
            # print f2, url_2
            if not f1:
                self.post_link()
            elif not f2:
                self.date -= 1
                self.post_link()

    def get_info(self):
        self.date, self.num = self.ct.get_info()

    def post_link(self):
        self.ct.save_link([self.date, self.num])


class Spider_controller(object):
    def __init__(self):
        self.now_date, self.now_num = getLastLink()
        self.now_date = Date(self.now_date)
        self.last_num = self.now_num
        self.last_date = self.now_date
        self.spider_num = 5
        self.max_dis = 400

    def get_info(self):
        self.now_num -= 1
        if self.last_num - self.now_num > self.max_dis:
            self.now_num = self.last_num
            self.now_date -= 1
        print str(self.now_date) + ' ' + str(self.now_num)
        return self.now_date, self.now_num

    def save_link(self, info):
        if str(info[0]) != str(self.now_date):
            self.now_date, self.now_num = info[0], info[1]
        self.last_date, self.last_num = info[0], info[1]
        with open(LINK_FILE_PATH, 'a+') as f:
            f.write(getUrl(info[0], info[1])+'\n')

    def run(self):
        spider_pool = [Links_spider(self) for i in range(self.spider_num)]
        try:
            for each in spider_pool:
                thread.start_new_thread(each.run, ())
        except:
            print 'erro'
a = Spider_controller()
a.run()
while 1:
    pass