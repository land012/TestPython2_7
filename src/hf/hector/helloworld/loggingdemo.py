__author__ = 'xudazhou'

import logging

log = logging.getLogger("loggingdemo")
log.setLevel(logging.DEBUG)

consoleHd = logging.StreamHandler()
# consoleHd.setLevel(logging.DEBUG)
consoleHd.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
log.addHandler(consoleHd)
print("1")
log.info("Hello logging")
log.warning("Hello logging warning")
print("2")