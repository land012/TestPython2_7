# coding:utf-8
__author__ = 'xudazhou'


def fn1():
    dict1 = dict()
    dict1["k1"] *= 2
    print(dict1["k1"])


def test2():
    dict1 = dict()
    dict1.setdefault("k1", [0, 0])
    dict1["k1"][0] = "a"
    dict1["k1"][1] = "b"
    dict1.setdefault("k2", [0, 0])
    dict1["k2"][0] = "c"
    dict1["k2"][1] = "d"

    """
    c
    a
    """
    for k in dict1.iteritems():
        print(k[1][0])


def test3():
    dict1 = {"k1": "v1", "k2": "v2", "k3": "v3"}
    list1 = sorted(dict1.iteritems(), key=lambda t: t[1])
    print(list1)  # [('k1', 'v1'), ('k2', 'v2'), ('k3', 'v3')]
    dict2 = dict(list1[:2])
    for k, v in dict2.iteritems():
        print("%s %s" % (k, v))


def test4():
    """
    遍历相关
    :return:
    """
    dict1 = {"k1": "v1", "k2": "v2"}
    print(type(dict1.items()))  # <type 'list'>
    print(type(dict1.iteritems()))  # <type 'dictionary-itemiterator'>


def test5():
    """
    输出的 key 顺序与初始化无关
    没能验证 每次执行key的顺序都不一样
    :return:
    """
    dict1 = {"k1": "v1", "k3": "v3", "k2": "v2", "k12": "v2", "k23": "v2"}
    dict2 = {"k1": "v1", "k3": "v3", "k2": "v2", "k12": "v2", "k23": "v2"}
    dict3 = {"k1": "v1", "k3": "v3", "k2": "v2", "k12": "v2", "k23": "v2"}
    for k in dict1.keys():
        print k,  # k3 k2 k1 k23 k12
    print

    for k in dict2.keys():
        print k,
    print

    for k in dict3.keys():
        print k,


if __name__ == "__main__":
    test5()
