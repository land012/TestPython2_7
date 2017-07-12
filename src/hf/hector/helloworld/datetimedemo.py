#coding:utf-8

import datetime
import time

__author__ = 'xudazhou'

# date
"""
# today() 相当于 Java 的静态方法，直接用类名就能调用，而不用 Object
today = datetime.date.today()
todayStr = today.strftime("%Y-%m-%d")
print(today)  # 2016-12-05
print(todayStr)  # 2016-12-05

yesterday = today + datetime.timedelta(days=-1)
print(yesterday)  # 2016-12-04

st1 = time.strptime("2016-12-02", "%Y-%m-%d")
dt1 = datetime.date.fromtimestamp(time.mktime(st1))
print(dt1)
"""
"""
date1 = datetime.date(2014, 4, 5)
print(date1)  # 2014-04-05
print(date1.strftime("%Y-%m-%d"))  # 2014-04-05
print(date1.today())  # 2016-12-05
"""

dt1 = datetime.datetime.strptime("2015-12-01 3:5:15", "%Y-%m-%d %H:%M:%S")
print(dt1.today())  # 2016-12-05 22:39:01.821000
print(dt1.strftime("%Y-%m-%d %H:%M:%S"))  # 2015-12-01 03:05:15
print(dt1.strftime("%Y-%m-%d"))  # 2015-12-01
