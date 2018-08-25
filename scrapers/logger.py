import logging
from time import gmtime, strftime
import re
from colorama import Fore, Back, Style, init

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

ignorewarnings = False


def init_logger (name, log_file, level=logging.INFO):
    """Function setup as many loggers as you want"""

    handler = logging.FileHandler(log_file, 'a', 'utf-8')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

genericlogger = init_logger('genericlogger', 'wikilog.log', logging.INFO)
errorlogger = init_logger('errorlogger', 'wikierrors.log', logging.INFO)

init()
def log(message):
    if not ignorewarnings:
        time_now = strftime("%d %b %Y %H:%M:%S", gmtime())
        print(f"{Fore.YELLOW}{time_now} MESSAGE:{Style.RESET_ALL} {message}")
    genericlogger.info(message)

def errorlog(message):
    if not ignorewarnings:
        time_now = strftime("%d %b %Y %H:%M:%S", gmtime())
        print(f"{Back.RED}{time_now} ERROR:{Style.RESET_ALL} {Fore.RED}{message}{Style.RESET_ALL}")
    errorlogger.info(f"ERROR: {message}")

