# coding: utf-8
"""
# Created by xudazhou at 2019/10/15
"""
import os
import sys
import logging
import time


logging.basicConfig(level=logging.INFO,
                    format='%(name)s %(asctime)s %(levelname)s %(filename)s(%(lineno)d) - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


if __name__ == "__main__":
    logging.info("main pid {}".format(sys.argv[1]))
    os.kill(int(sys.argv[1]), 9)

    time.sleep(1)

    # kill 掉主进程，子进程也被 kill,这句不会执行
    logging.info("i am hello3 end")
