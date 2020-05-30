# coding: utf-8
"""
# Created by xudazhou at 2019/9/23
进程通信
Manager
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
    while p_event.is_set():
        time.sleep(1)
        # AttributeError: 'module' object has no attribute 'getppid'
        # windows 中没有 ppid
        # print "i am child process {}, pid={}, ppid={}".format(p_arg1, os.getpid(), os.getppid())
        print "i am child process {}, pid={}".format(p_arg1, os.getpid())


if __name__ == "__main__":
    print "i am main process, pid={}".format(os.getpid())
    mgr = multiprocessing.Manager()
    flag = mgr.Event()
    flag.set()
    p1 = multiprocessing.Process(target=proc_run, args=('tom', flag))
    p1.start()  # 异步执行

    time.sleep(3)
    flag.clear()
    """
    Process Process-2:
    Traceback (most recent call last):
      ...
      File "D:\_python\TestPython27\threaddemo\processdemo5.py", line 19, in proc_run
        while p_event.is_set():
      File "D:\ProgramDev\Python27\lib\multiprocessing\managers.py", line 1009, in is_set
        return self._callmethod('is_set')
      File "D:\ProgramDev\Python27\lib\multiprocessing\managers.py", line 758, in _callmethod
        conn.send((self._id, methodname, args, kwds))
    IOError: [Errno 232]
    """
    p1.join()  # 不加这行会抛异常，似乎是因为子进程退出，主进程连接不到子进程？
    print "main process end"
