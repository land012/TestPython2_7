# coding: utf-8

import logging
import unittest

__author__ = 'xudazhou'


class LoggingDemo(unittest.TestCase):

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s (%(lineno)d) - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    @staticmethod
    def test1():
        logging.debug("haha")  # 这行不会打印

        logging.info("heihei")

        tup1 = ("a", "b", 1)
        logging.info(tup1)

        i1 = 5
        logging.info("i1=%s", i1)

    @staticmethod
    def test2():
        """多个参数"""
        logging.info("%s %s", "s1", "s2")
        list1 = ["a", "b"]
        logging.info("list1=%s", list1)

    @staticmethod
    def test3():
        """dict 参数"""
        logging.info("%(k1)s %(k2)s", {"k1": "v1", "k2": "v2"})

    @staticmethod
    def test4():
        """XXX 似乎不支持两种方式混合使用"""
        logging.info("%(k1)s %s %s", ("s1", "s2"), {"k1": "v1", "k2": "v2", "k3": "v3"})
