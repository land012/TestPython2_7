# coding:utf-8
__author__ = 'xudazhou'

str1 = "a"

'''
str2 = """
    i am b,
    you are """ \
       + str1 + """. """ \
       + " haha " \
       + str(2)

print(str2)
'''

'''
# split
str3 = "a	b	c"
arr3 = str3.strip().split()
print(arr3[1])  # b
print(arr3[len(arr3) - 1])  # c
arr3_2 = str3.split('\t', 1)  # 做1次分割，最多分割为两个字符串
print(len(arr3_2))  # 2
'''

'''
# 是否是数字
str1 = "123"
print(str1.isdigit())  # True
str2 = "1.1"
print(str2.isdigit())  # False
str3 = "-2"
print(str3.isdigit())  # False
'''

# str 也是序列
"""
str1 = "abc"
print(str1[0])
print(str1[1])
"""

"""
str2 = "5"
print({'0': 0, '3': 3, '4': 4, '5': 5, '6': 6}[str2])
"""

"""
# startwith
str1 = " abc"  # 以空格打头
str2 = "    abc"  # 以 制表符打头
print(str1.startswith("\s"))  # False
print(str1.startswith(" "))  # True
print(str2.startswith("\s"))  # False
print(str2.startswith("\t"))  # False
print(str2.startswith(" "))  # True
print(str2.startswith((" ", "   ")))  # True
"""

# print("\tabc")  # 打打印为制表符


def test1():
    l_str = "a %s b %s" % ("1", "2")
    print(l_str)


def test2():
    l_str = "a,b,,d"
    l_list = l_str.split(",")
    print(len(l_list))  # 4


def test3():
    l_str = " abcde "
    print(l_str.rstrip())
    print(l_str.lstrip())


if __name__ == "__main__":
    test3()
