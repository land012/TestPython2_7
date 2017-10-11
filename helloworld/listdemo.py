# coding: utf-8
# 冒号: 前面不能有空格
__author__ = 'xudazhou'


def test1():
    l_list1 = ["a", "b", "c"]
    str1 = ",".join(l_list1)
    print(str1)  # a,b,c


def test3():
    """
    append 一个 list
    :return:
    """
    l_list1 = list(["a", "aa"])
    l_list1.append(["b", "c"])  # ['a', 'aa', ['b', 'c']]
    print(l_list1)


def test4():
    l_list1 = list(["a", "aa"])
    l_list1 = l_list1 + list(["b", "c"])
    print(l_list1)  # ['a', 'aa', 'b', 'c']

if __name__ == "__main__":
    test4()
