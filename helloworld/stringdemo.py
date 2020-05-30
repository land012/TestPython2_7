# coding:utf-8
from __future__ import print_function
import unittest

__author__ = 'xudazhou'


class StringDemo(unittest.TestCase):

    @staticmethod
    def test1():
        str1 = "a b c"
        if "a b c" == str1:
            print("1")  # 1
        else:
            print("0")

    @staticmethod
    def test_zh():
        str1 = "1我"
        print(len(str1))  # 4
        print(str1[1:2])  # �
        print(str1[1:4])  # 我
        print(ord(str1[0:1]))  # 49

    @staticmethod
    def test_split():
        str3 = "a	b	c"
        # TypeError: split() takes no keyword arguments
        # str3_arr = str3.split("\t", maxsplit=1)

        # TypeError: split() takes no keyword arguments
        # str3_arr = str3.split(sep="\t", maxsplit=1)

        # 不需要指定 keyword
        str3_arr = str3.split("\t", 1)

        # 不支持正则表达式
        str3_arr2 = str3.split("\s")
        for e in str3_arr2:
            print(e)  # a	b	c

    @staticmethod
    def test_split2():
        """
        默认分隔符 支持 制表符，换行
        :return:
        """
        str1 = "a	b c\nd"
        str1_arr = str1.split()
        print(len(str1_arr))  # 4


str1 = "a"

'''
str2 = """
    i am b,
    you are """ \
       + str1 + """. """ \
       + " haha " \
       + str(2)

print(str2)
'''

'''
# split
str3 = "a	b	c"
arr3 = str3.strip().split()
print(arr3[1])  # b
print(arr3[len(arr3) - 1])  # c
arr3_2 = str3.split('\t', 1)  # 做1次分割，最多分割为两个字符串
print(len(arr3_2))  # 2
'''

'''
# 是否是数字
str1 = "123"
print(str1.isdigit())  # True
str2 = "1.1"
print(str2.isdigit())  # False
str3 = "-2"
print(str3.isdigit())  # False
'''

# str 也是序列
"""
str1 = "abc"
print(str1[0])
print(str1[1])
"""

"""
str2 = "5"
print({'0': 0, '3': 3, '4': 4, '5': 5, '6': 6}[str2])
"""

"""
# startwith
str1 = " abc"  # 以空格打头
str2 = "    abc"  # 以 制表符打头
print(str1.startswith("\s"))  # False
print(str1.startswith(" "))  # True
print(str2.startswith("\s"))  # False
print(str2.startswith("\t"))  # False
print(str2.startswith(" "))  # True
print(str2.startswith((" ", "   ")))  # True
"""

# print("\tabc")  # 打打印为制表符


def test1():
    l_str = "a %s b %s" % ("1", "2")
    print(l_str)


def test2():
    l_str = "a,b,,d"
    l_list = l_str.split(",")
    print(len(l_list))  # 4


def test3():
    l_str = " abcde "
    print(l_str.rstrip())
    print(l_str.lstrip())



