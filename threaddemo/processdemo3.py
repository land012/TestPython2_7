# coding: utf-8
"""
# Created by xudazhou at 2019/9/23
进程通信
验证 变量的方式
"""
import multiprocessing
import os
import time


def proc_run(p_arg1, p_event):
    """
    在任务管理器 中可以看到单独的进程
    :param p_event:
    :param p_arg1:
    :return:
    """
    while p_event:
        time.sleep(2)
        # AttributeError: 'module' object has no attribute 'getppid'
        # windows 中没有 ppid
        # print "i am child process {}, pid={}, ppid={}".format(p_arg1, os.getpid(), os.getppid())
        print "i am child process {}, pid={}".format(p_arg1, os.getpid())


if __name__ == "__main__":
    print "i am main process, pid={}".format(os.getpid())
    flag = True
    p1 = multiprocessing.Process(target=proc_run, args=('tom', flag))
    p1.start()  # 异步执行

    time.sleep(3)
    flag = False  # 这里的修改，不会传给子进程，无法用这种试结束子进程
    print "main process end"
