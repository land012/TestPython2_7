# coding:utf-8
__author__ = 'xudazhou'

"""
读文件 然后再写回
"""
f = open("hello2.txt", "r+")
text = ""
for line in f:
    if "hello jim" == line.strip():
        text += "jack\n"
    else:
        text += line

print(text)

f.seek(0)
f.truncate()
f.write(text)

f.close()
