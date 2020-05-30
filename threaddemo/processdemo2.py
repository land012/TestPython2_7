# coding: utf-8
"""
# Created by xudazhou at 2019/9/23
"""
import multiprocessing
import os
import time
import logging
import sys


logging.basicConfig(level=logging.INFO,
                        format='%(name)s %(asctime)s %(levelname)s (%(lineno)d) - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')


def proc_run(p_arg1):
    """
    在任务管理器 中可以看到单独的进程
    :param p_arg1:
    :return:
    """
    # exit(1)  # 仅退出子进程，如何退出主进程？？
    # os._exit(1)  # 仅退出子进程，如何退出主进程？？
    sys.exit(1)  # 仅退出子进程，如何退出主进程？？
    print "i am child process {}, pid={}".format(p_arg1, os.getpid())


if __name__ == "__main__":
    logging.info("i am main process, pid={}".format(os.getpid()))
    p1 = multiprocessing.Process(target=proc_run, args=('tom', ))
    p1.start()
    time.sleep(2)
    logging.info("main process end")
