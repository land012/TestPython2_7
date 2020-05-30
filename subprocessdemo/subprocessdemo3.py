# coding: utf-8
"""
# Created by xudazhou at 2019/9/23
可以在 subprocess kill 主进程
"""
import subprocess
import os
import logging
import time


logging.basicConfig(level=logging.INFO,
                    format='%(name)s %(asctime)s %(levelname)s (%(lineno)d) - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


if __name__ == "__main__":
    logging.info("i am main begin")
    p = subprocess.Popen(["D:\ProgramDev\Python27\python.exe", "hello3.py", str(os.getpid())])
    time.sleep(5)
    logging.info("i am main end")
