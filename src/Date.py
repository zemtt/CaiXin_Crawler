# -*- coding:utf-8 -*-
import time


def Stamp2Date(stamp):
    return time.strftime('%Y-%m-%d', time.localtime(int(stamp)))


def Date2Stamp(date):
    timeArray = time.strptime(date, "%Y-%m-%d")
    return int(time.mktime(timeArray))


class Date(object):
    def __init__(self, date='2000-1-1'):
        if isinstance(date, str):
            self.stamp = Date2Stamp(date)
        elif isinstance(date, int):
            self.stamp = date

    def __add__(self, i):
        return Date(self.stamp + i*86400)

    def __iadd__(self, i):
        return Date(self.stamp + i*86400)

    def __sub__(self, i):
        return Date(self.stamp - i*86400)

    def __isub__(self, i):
        return Date(self.stamp - i*86400)

    def __repr__(self):
        return Stamp2Date(self.stamp)
