# coding: utf-8
"""
# Created by xudazhou at 2019/9/21
"""

if __name__ == "__main__":
    print bool()  # False
    print bool("")  # False
    print bool(" ")  # True

    print bool(-1)  # True
    print bool(0)  # False
    print bool(1)  # True
    print bool(2)  # True
    print bool(None)  # False
    print bool("false")  # True
