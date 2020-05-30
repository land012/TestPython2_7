# coding: utf-8
"""
# Created by xudazhou at 2019/10/10
"""
import time
import logging
logging.basicConfig(level=logging.INFO,
                            format='%(name)s %(asctime)s %(levelname)s (%(lineno)d) - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')


logging.info("i am {}".format(__file__))

time.sleep(3)

exit(-23)
