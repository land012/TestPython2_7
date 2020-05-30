# coding: utf-8
"""
# Created by xudazhou at 2019/11/29
"""
import unittest
import hashlib


class HashlibTest(unittest.TestCase):

    @staticmethod
    def test1():
        print hashlib.md5("www.baidu.com").hexdigest()
