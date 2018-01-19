# coding:utf-8

import module1
import traceback
import sys

__author__ = 'xudazhou'


def fn1(p_list):
    """
    传引用!!
    :param p_list:
    :return:
    """

    p_list.append("a")


def fn2(p_a):
    """
    传值
    :param p_a:
    :return:
    """
    p_a = 2


def test1():
    """
    :return:
    """
    l_list = []
    fn1(l_list)
    print(l_list)  # ['a']

    a = 1
    fn2(a)
    print(a)  # 1


if __name__ == "__main__":
    # test1()
    try:
        module1.fn3()
    except AttributeError:
        # traceback.print_exc(file=sys.stderr)
        print(traceback.format_exc())
        print("====================== 1 =========================")
        ex_i = sys.exc_info()
        print(ex_i)
        print("====================== 2 =========================")
        exc_traceback = ex_i[2]
        # print(exc_traceback.tb_lineno)
        # print(traceback.format_tb(exc_traceback))
        arr = traceback.extract_tb(exc_traceback)
        print(arr)
        pass

    print("================ end ==================")
