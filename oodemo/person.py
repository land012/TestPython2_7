# coding: utf-8
"""
# Created by xudazhou at 2019/9/20
类中的静态方法引用
"""


class Person:

    ID = 1

    def __init__(self):
        self.age = 1

    def get_age(self):
        return self.age_add(self.age)  # 使用静态方法，要加 self

    @staticmethod
    def age_add(p_v):
        p_v += 1
        return p_v


if __name__ == "__main__":
    p = Person()
    print p.get_age()  # 2
    print Person.ID
