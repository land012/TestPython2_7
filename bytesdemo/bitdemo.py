# coding: utf-8
import struct
import unittest
import binascii


class BitDemo(unittest.TestCase):

    @staticmethod
    def test1():
        str1 = '\0abc'
        b = struct.unpack('>I', str1)[0] & 0xffffffff
        print hex(b)

    @staticmethod
    def test2():
        i = 5
        print bin(i)  # 0b101
        str1 = str(i)
        print type(str1)  # <type 'str'>
        hex1 = binascii.hexlify(str1)
        print type(hex1)  # <type 'str'>
        print hex1  # 35
        j = ~i
        print j  # -6
        print bin(j)  # -0b110
        print bin(j & 0xffffffff)  # 0b11111111111111111111111111111010

    @staticmethod
    def test3():
        i = 255
        print bin(i)  # 0b11111111
        print bin(-1)  # -0b1
