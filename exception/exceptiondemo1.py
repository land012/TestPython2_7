# coding: utf-8

import sys
import traceback

__author__ = 'xudazhou'


def test1():
    try:
        raise Exception
    except Exception, e:
        traceback.print_exc()
        ex_info = sys.exc_info()
        print(ex_info)
        print(ex_info[2].tb_lineno)  # 10


if __name__ == "__main__":
    test1()
