import os
import sys
import ctypes
import logging
from colorlog import ColoredFormatter
from colorama import Fore

def restart():
    """ Перезагружает бота. """
    print(f"{Fore.WHITE}Перезапуск бота...\n")
    os.execv(sys.executable, [sys.executable] + sys.argv)
    exit()

def set_title(title):
    """
    Устанавливает заголовок консоли (кросс-платформенно).
    Работает на Windows, Linux и macOS.
    """
    sys.stdout.write(f"\x1b]2;{title}\x07")
    sys.stdout.flush()

def setup_logger():
    """ 
    Настраивает глобальный логгер. 
    """
    LOG_FORMAT = "%(log_color)s[%(asctime)s] %(levelname)-8s %(message)s"
    formatter = ColoredFormatter(
        LOG_FORMAT,
        datefmt="%Y.%m.%d %H:%M:%S",
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'white',
            'WARNING': 'lightyellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        },
        secondary_log_colors={},
        style='%'
    )
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    logger.addHandler(console_handler)
