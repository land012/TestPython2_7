# coding:utf-8

import person_pb2

__author__ = 'xudazhou'

"""
用 java 写 protobuf 文件
用 python 解析
"""

if __name__ == '__main__':
    person = person_pb2.Person()

    f1 = open("E:\\TDDOWNLOAD\\file3.dat", "rb")
    person.ParseFromString(f1.read())
    f1.close()

    """
    id: 12
    name: "asuka"
    """
    print(person.__str__())
