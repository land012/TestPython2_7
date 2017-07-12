# coding: utf-8
__author__ = 'xudazhou'
"""
迭代类
斐波那契
"""


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def next(self):
        k = self.a
        self.a = self.b
        self.b = self.b + k

        if self.a > 10:
            raise StopIteration()

        return self.a


if __name__ == "__main__":
    for i in Fib():
        print(i)
