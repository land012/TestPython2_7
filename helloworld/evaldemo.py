# coding: utf-8

import unittest


def fn1():
    return "hello fn1"


def fn2(p_p1):
    print(p_p1)


class EvalDemo(unittest.TestCase):

    @staticmethod
    def test1():
        print(eval("fn1()"))  # hello fn1

    @staticmethod
    def test2():
        eval("fn2(\"test fn2\")")  # test fn2
