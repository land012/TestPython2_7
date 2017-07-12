#coding:utf-8

__author__ = 'xudazhou'

import os

# print(os.name)  # nt

# 报错 AttributeError: 'module' object has no attribute 'uname'
# print(os.uname())

# 执行本地命令 这个命令已过期 Deprecated
'''
result = os.popen("ipconfig")
for line in result:
    print(line)
'''

# 执行本地命令
'''
r1 = os.system("echo haha")
print("r1=%s" % r1)  # r1=0
'''

'''
result = os.popen('curl -s -I "http://api400.web4008.com/interface/apioutline/get_mp3.ashx?RecID=200172192516&StartDate=20160818134431"')
for line in result:
    print(line)
'''

print(os.environ.get("JAVA_HOME"))  # D:\ProgramDev\Java\jdk1.8.0_65
print(os.environ["M2_HOME"])  # D:\ProgramDev\apache-maven-3.2.3
