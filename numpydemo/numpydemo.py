# coding: utf-8
"""
# Created by xudazhou at 2019/9/27
"""
import unittest
import numpy
import numpy.random


class NumpyDemo(unittest.TestCase):

    @staticmethod
    def test1():
        list1 = numpy.random.randint(3, size=5)
        print type(list1)  # <type 'numpy.ndarray'>
        print list1  # [1 2 1 0 2]

        list2 = numpy.sort(list1)
        print type(list2)
        print list2  # [0 1 1 2 2]

    @staticmethod
    def test2():
        num_frames = 155
        num_select = 8
        quotient = num_frames // num_select
        print quotient  # 19
        list1 = range(num_select)  # <type 'list'>
        print type(list1)
        list11 = numpy.multiply(list1, quotient)
        print list11
        list2 = list11 + numpy.random.randint(quotient, size=num_select)
        print list2  # [ 14  25  52  61  84 104 118 136]
        list2 += 1
        print list2
