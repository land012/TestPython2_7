# coding: utf-8
"""
# Created by xudazhou at 2019/9/23
"""
import multiprocessing
import os
import time
import random
import logging


logging.basicConfig(level=logging.INFO,
                        format='%(name)s %(asctime)s %(levelname)s (%(lineno)d) - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')


def hello(p_name):
    logging.info("i am {} begin".format(os.getpid()))
    time.sleep(random.randint(1, 4))
    logging.info("hello {}, i am {}".format(p_name, os.getpid()))


if __name__ == "__main__":
    list1 = ['tom', 'jim', 'cat', 'lily', 'lucy', 'dog']
    pool = multiprocessing.Pool(3)
    pool.map(hello, list1)  # 子进程之间是异步的，和主进程是同步的
    pool.close()
    logging.info("main {}".format(os.getpid()))
