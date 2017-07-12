#coding:utf-8
__author__ = 'xudazhou'

# 追加写入
"""
file1 = open("E:\TDDOWNLOAD\helloworld.txt", "a")
file1.write("你好\n")
"""

'''
file1 = open("E:\TDDOWNLOAD\helloworld.txt", "r")
print(file1.read())
'''


def bytestoint(bytearr):
    i1 = bytearr[0] << 24
    i2 = bytearr[1] << 16
    i3 = bytearr[2] << 8
    i4 = bytearr[3]
    return i1 + i2 + i3 + i4

# 读取二进制文件
file1 = open("E:\\TDDOWNLOAD\\file1.dat", mode="r")
num_str1 = file1.read(4)
print(len(num_str1))  # 4
print(type(num_str1))  # <type 'str'>

byte1 = bytearray(num_str1)
print(type(byte1))  # <type 'bytearray'>
print(len(byte1))  # 4
len1 = bytestoint(byte1)
print(len1)  # 110

value1 = file1.read(len1)
print(value1)

len2 = bytestoint(bytearray(file1.read(4)))
print("len2=%s" % len2)  # len2=6
str2 = file1.read(len2)
print(str2)

