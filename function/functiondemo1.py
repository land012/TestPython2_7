# coding:utf-8
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
    test1()
