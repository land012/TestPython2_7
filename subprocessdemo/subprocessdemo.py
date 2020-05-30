# coding: utf-8
"""
# Created by xudazhou at 2019/9/23
"""
import subprocess


if __name__ == "__main__":
    # p = subprocess.Popen("echo %cd%", shell=True)
    p = subprocess.Popen("exit -23", shell=True)
    p.communicate()
    print p.returncode
    print "i am main"
