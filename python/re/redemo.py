import re

__author__ = 'xudazhou'


def test1():
    print(re.match("^a", "abc") and True)  # True
    print(re.match("a", "abc") and True)  # True
    print(re.match("a.*", "abc") and True)  # True
    print(not re.match("a.*", "abc"))  # False
    print(re.match("b", "abc") and True)  # None
    print(not re.match("b", "abc"))  # True


def test2():
    print(re.match("\s", " a") and True)  # True
    print(re.match("\s", "  a") and True)  # True
    print(re.match("\s", "b  a") and True)  # None
    print(re.match("^\s|#", "\ta") and True)  # True
    print(re.match("^\s|#", "#\ta") and True)  # True
    print(re.match("^\s|#", "x#\ta") and True)  # None


if __name__ == "__main__":
    test2()
