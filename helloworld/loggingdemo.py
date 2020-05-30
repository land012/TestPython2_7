import logging
import unittest

__author__ = 'xudazhou'


class LoggingDemo(unittest.TestCase):

    @staticmethod
    def test1():
        log = logging.getLogger("loggingdemo")
        log.setLevel(logging.DEBUG)

        consoleHandler = logging.StreamHandler()
        # consoleHd.setLevel(logging.DEBUG)
        consoleHandler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
        log.addHandler(consoleHandler)

        print("1")
        log.info("Hello\nlogging")

        exit(1)

        log.warning("Hello logging warning")
        print("2")

    @staticmethod
    def test2():
        logging.basicConfig(filename="logs/server.log",
                            level=logging.INFO,
                            format='%(name)s %(asctime)s %(levelname)s (%(lineno)d) - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

        logging.info("hello logging file")
