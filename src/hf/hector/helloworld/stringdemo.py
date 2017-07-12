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

str1 = "abc"
print(str1[0])
print(str1[1])
