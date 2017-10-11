__author__ = 'xudazhou'

f = open("E:\TDDOWNLOAD\\temp\\1.txt", "r")
list1 = f.readlines()

print(type(list1))  # <type 'list'>
print(list1)  # ['haha\n', 'wo shi ya ge xiao wang zi,ni shi yi ge da sha zi.\n', 'heiei\n']
