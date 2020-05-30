# coding: utf-8
"""
# Created by xudazhou at 2019/9/10
"""

import unittest


class RangeDemo(unittest.TestCase):

    @staticmethod
    def test1():
        print range(10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        print type(range(10)[1])  # <type 'int'>

    @staticmethod
    def test2():
        """

        :return:
        """
        # 5 4 3 2 1 0
        for i in range(5, -1, -1):
            print i,
