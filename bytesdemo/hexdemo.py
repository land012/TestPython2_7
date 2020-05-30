# coding: utf-8
import unittest


class HexDemo(unittest.TestCase):

    @staticmethod
    def test1():
        # ord 返回 十进制 ascii
        # hex 返回 int 的 十六进制
        print hex(ord('a'))  # 0x61
        print unichr(0xa0)

    @staticmethod
    def test2():
        """
        ord
        可以将 unicode,ascii 字符，转为十进制数字
        但不能转汉字
        :return:
        """
        print unicode(u'\u2020')  # †
        print ord(u'\u2020')  # 8224
        print hex(8224)  # 0x2020

        print unicode(u'\u0174')  # Ŵ
        print ord(u'\u0174')  # 372

        print unicode(u'\u8382')  # 莂
        print ord(u'\u8382')  # 33666
        print unicode(u'\u5C4C')  # 屌
        print ord(u'\u5C4C')  # 23628


# for i in range(67, )
