# coding: utf-8
"""
# Created by xudazhou at 2019/9/10
"""
import unittest


class StringFormatDemo(unittest.TestCase):

    @staticmethod
    def test1():
        print "%05d" % 12  # 00012

    @staticmethod
    def test2():
        list1 = ["a", "b"]
        print "list={}".format(list1)

    @staticmethod
    def test3():
        print "{:0>5}".format(3)  # 00003
        print "{:0>5}".format(123456)  # 123456
