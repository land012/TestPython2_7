#! /usr/bin/env python
# coding:utf-8
"""引用父目录的 模块，虽然报错，但是可以引用的父目录的模块"""


import sys

sys.path.append("..")

import module2

__author__ = 'xudazhou'

reload(sys)
# sys.setdefaultencoding("gbk")

module2.greet()

print("我是 hellogreet")  # 中文输出乱码

print("finish!")

# 打印当前模块的 docStrings
print(__doc__)
