# coding:utf-8
__author__ = 'xudazhou'
"""
引入子目录中的模块
"""

import common.module1

common.module1.fun1()

# 这两种 if 都会返回 false
str1 = ""
str1 = None

if str1:
    print "yes"
else:
    print "no"  # no

str1 = "a"
if str1:
    print "yes"  # yes
else:
    print "no"


