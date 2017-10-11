__author__ = 'xudazhou'

"""
读文件 然后再写回
"""
f = open("E:\TDDOWNLOAD\hello.txt", "r")
text = ""
for line in f:
    if "hello jim" == line.strip():
        text += "Hello jack\n"
    else:
        text += line
print(text)
f.close()

f1 = open("E:\TDDOWNLOAD\hello.txt", "w")
f1.write(text)
f1.flush()
f1.close()
