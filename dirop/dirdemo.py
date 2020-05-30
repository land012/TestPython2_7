# coding: utf-8
import unittest
import os
import sys


class DirDemo(unittest.TestCase):

    @staticmethod
    def test1():
        print sys.getdefaultencoding()  # ascii

        list1 = os.listdir("E:\TDDOWNLOAD")
        print list1

        for i in list1:
            print type(i)  # <type 'str'>
            print i.decode("gbk")  # 正常显示中文

    @staticmethod
    def test2():
        path = "E:\TDDOWNLOAD"
        print os.path.basename(path)  # TDDOWNLOAD
        print os.path.dirname(path)  # E:\
