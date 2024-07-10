import logging

from myLogHandler import LogHandler


log_handler = LogHandler(log_dir='logs',log_file='application.log',level=logging.DEBUG)
logger = log_handler.get_logger()


logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")


try:
    1 / 0
except ZeroDivisionError as e:
    logger.exception("Exception occurred")