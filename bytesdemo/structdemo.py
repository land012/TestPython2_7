# coding: utf-8

import struct
import unittest
import binascii


class StructTest(unittest.TestCase):

    @staticmethod
    def test1():
        print struct.unpack('B', "a")  # (97,)

        str2 = struct.pack('B', 142)
        print str2
        print struct.unpack('B', str2)

    @staticmethod
    def test2():
        str1 = struct.pack('>I', 65)
        print str1  # A
        print len(str1)  # 4

    @staticmethod
    def test3():
        bytes1 = struct.pack('>I', 4294967295)
        print type(bytes1)  # <type 'str'>
        print bytes1

    @staticmethod
    def test3():
        bytes1 = struct.pack('>i', -1)
        print type(bytes1)  # <type 'str'>，实际上是字节数组类型
        print bytes1  # 乱码
        print binascii.hexlify(bytes1)  # ffffffff

    @staticmethod
    def test4():
        bytes1 = struct.pack('s', "A")
        print type(bytes1)  # <type 'str'>，实际上是字节数组类型
        print bytes1  # A
        hex1 = binascii.hexlify(bytes1)
        print type(hex1)  # <type 'str'>
        print hex1  # 41

    @staticmethod
    def test4_2():
        """
        反向执行 test4
        :return:
        """
        hex1 = "41"
        bin1 = binascii.unhexlify(hex1)
        str1 = struct.unpack('s', bin1)
        print str1  # ('A',)

    @staticmethod
    def test_writefile():
        l_bytes = struct.pack("!I", 32353)
        print len(l_bytes)  # 4
        f = open("1.txt", mode="wb")
        f.write(l_bytes)
        f.close()
