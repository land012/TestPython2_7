# coding:utf-8
__author__ = 'xudazhou'

"""
这种方式，会逐行读取，pos 会逐渐增加

边读边写，当写时，会覆盖从当前位置往后的数据
"""
f = open("hello.txt", "r+")

pos = 0

line = f.readline()
last_pos = pos
pos = f.tell()

while line != "":
    print(line)
    print(pos)
    print(last_pos)

    if "hello jim" == line.strip():
        f.seek(last_pos, 0)
        f.write("hello jack\n")
        break

    line = f.readline()
    last_pos = pos
    pos = f.tell()

f.close()

