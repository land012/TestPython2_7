import datetime
import unittest
import sys

__author__ = 'xudazhou'


class PrintDemo(unittest.TestCase):

    @staticmethod
    def test1():
        print "a",

        print "gg", ""

        print("b")

        print "%s" % "abc",

        print("ef")

    @staticmethod
    def test2():
        a = 80
        print a,

    @staticmethod
    def test3():
        # k1-v1 | END
        print "%s-%s" % ("k1", "v1"), '|', 'END',

    @staticmethod
    def test4():
        print "this is {food}".format(food="bread")  # this is bread

    @staticmethod
    def test5():
        # 2016-12-22 15:38:42
        print "%s | %s" % (datetime.datetime.fromtimestamp(1482392322), "haha")
        print "%s | %s" % (datetime.datetime.fromtimestamp(1482392322.1), "haha")

    @staticmethod
    def test6():
        list1 = ["a", "b"]
        print("%s" % list1)  # ['a', 'b']

    @staticmethod
    def test7():
        print "abc"
        print >> sys.stderr, "def"
