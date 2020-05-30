# coding: utf-8
"""
# Created by xudazhou at 2020/1/4
"""
from mobiparse import Mobi

mobi = Mobi(r"E:\TDDOWNLOAD\1.mobi")
html, images = mobi.parse()
# print html

f = open("1.html", mode="w")
f.write(html)
f.close()
