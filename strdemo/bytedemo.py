# coding:utf-8
import sys
import unittest

__author__ = 'xudazhou'

reload(sys)

sys.setdefaultencoding('utf-8')


class ByteDemo(unittest.TestCase):

    @staticmethod
    def test1():
        var1 = "hello"
        print type(var1)  # <type 'str'>

        b1 = b"world"
        print type(b1)  # <type 'str'>
        print b1  # world

        str1 = str(b1)
        print type(str1)  # <type 'str'>
        print(str1)  # world

        print(b1[0])  # w

        un1 = b1[0].decode()
        print type(un1)  # <type 'unicode'>
        print(un1)  # w

    @staticmethod
    def test2():
        str1 = "world"
        b2 = str1.encode(encoding='gbk')
        str2 = b2.decode(encoding='gbk')
        print(b2)  # world
        print(str2)  # world

        b3 = b"小李"
        print(b3)  # 小李
        print(b3[0:3])  # 小
        print(len(b3))  # 6

        print(bytes([2, 3, 6, 8]))

        # 必须有上面的 sys.setdefaultencoding('utf-8'),这句才能执行通过，否则报错
        print("小李".encode(encoding='utf-8'))  # 小李

        print("======================== 1 ==========================")

        ba1 = bytearray(b"Aworld")
        print(ba1)  # Aworld
        print(ba1[0])  # 65

        ba2 = bytearray("Bcd")
        print(ba2[0])  # 66
        # print(ba2[0].decode(encoding='utf-8'))  # 66

        ba3 = bytearray("我是小李")
        print(ba3[0])  # 230
        str3_3 = str(ba3[0])
        print(str3_3)  # 230

    @staticmethod
    def test43():
        b1 = b'124s'
        i1 = int(b1)  # ValueError: invalid literal for int() with base 10: '124s'
        print(i1)
