# coding:utf-8
__author__ = 'xudazhou'


def test1():
    """
    验证 boolean
    :return:
    """
    l_dict1 = {"a": 1, "b": 0}
    print(l_dict1.get("a") and True)  # True
    print(l_dict1.get("b") and True)  # 0
    print(l_dict1.get("c", 2))  # 2


if __name__ == "__main__":
    test1()
