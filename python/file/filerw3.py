# coding:utf-8
__author__ = 'xudazhou'

"""
tell
seek
for 的方式读文件，一次读出了全部文件内容
"""
f = open("hello.txt", "r+")
text = ""
# print(f.tell())
for line in f:
    # print(line)
    pos = f.tell()
    print(line.startswith(" "))  # 第二次 True
    print(line.endswith("\n"))  # 前两次 True，第三次 False
    print(pos)  # 这种方式永远打印 47，因为一开始就打开到了文件尾
    if "hello jim" == line.strip():
        f.seek(pos, 0)
        f.write("hello jack\n")
        break

f.close()

