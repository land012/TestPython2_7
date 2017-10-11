__author__ = 'xudazhou'

str1 = "abc"
i1 = iter(str1)

"""
a
b
c
"""
try:
    while True:
        print(i1.next())
except StopIteration as e:
    print("==" + str(e))  # ==


print(i1)  # <iterator object at 0x0267E670>
print(type(i1))  # <type 'iterator'>

