import logging

__author__ = 'xudazhou'


log = logging.getLogger("loggingdemo")
log.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
# consoleHd.setLevel(logging.DEBUG)
consoleHandler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
log.addHandler(consoleHandler)

print("1")
log.info("Hello logging")

exit(1)

log.warning("Hello logging warning")
print("2")
