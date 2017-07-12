# coding:utf-8

import person_pb2

__author__ = 'xudazhou'

"""
用 java 解析这个文件
"""

if __name__ == '__main__':
    print("main")
    person = person_pb2.Person()
    person.id = 11
    person.name = "hector"

    print(person.__str__())  # id: 11

    f1 = open("E:\\TDDOWNLOAD\\file2.dat", "wb")
    str1 = person.SerializeToString()
    print(str1)
    f1.write(str1)
    f1.flush()
    f1.close()
