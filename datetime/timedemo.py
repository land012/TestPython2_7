# coding: utf-8

import unittest
import time


class TimeDemo(unittest.TestCase):

    @staticmethod
    def test1():
        print(time.time())
