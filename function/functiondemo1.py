# coding:utf-8
__author__ = 'xudazhou'


def fn1(p_list):
    """
    传引用??
    :param p_list:
    :return:
    """

    p_list.append("a")


def test1():
    """
    :return:
    """
    l_list = []
    fn1(l_list)
    print(l_list)  # ['a']


if __name__ == "__main__":
    test1()
