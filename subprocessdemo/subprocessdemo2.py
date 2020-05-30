# coding: utf-8
"""
# Created by xudazhou at 2019/9/23
Popen 在创建对象时就会执行，且是异步执行
"""
import subprocess
import logging
import time


logging.basicConfig(level=logging.INFO,
                            format='%(name)s %(asctime)s %(levelname)s (%(lineno)d) - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')


if __name__ == "__main__":
    # p = subprocess.Popen("echo %cd%", shell=True)
    logging.info("i am main begin")
    p = subprocess.Popen("D:\ProgramDev\Python27\python.exe hello.py", shell=True)
    time.sleep(5)
    # p.communicate()
    print p.returncode
    logging.info("i am main")
