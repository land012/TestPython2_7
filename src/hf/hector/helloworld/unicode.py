# -*- coding: utf-8 -*-
'''
加上第一行，可以在注释中写中文
或者加上这句
#coding:utf-8
'''

__author__ = 'xudazhou'


# 中文
str1 = "<p>我是 Orochi %2B</p>"
# 必须指定编码，否则报错 UnicodeDecodeError: 'ascii' codec can't decode byte 0xe6 in position 3: ordinal not in range(128)
# 应该是因为使用了系统默认的 gbk 去编码
print(unicode(str1, "utf-8"))  # <p>我是 Orochi %2B</p>
