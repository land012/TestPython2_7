# coding: utf-8
"""
# Created by xudazhou at 2019/9/23
"""
import threading
import time


class MyThread(threading.Thread):

    def __init__(self, p_name):
        super(MyThread, self).__init__()
        self.arg1 = p_name

    def run(self):
        time.sleep(2)
        print "i am thread {}, {}".format(threading.currentThread().getName(), self.arg1)


if __name__ == "__main__":
    t1 = MyThread("tom")
    t1.start()
    print "i am main"
