"""
A comfier logging module.
"""

import logging
import sys
from logging import Logger, StreamHandler

from fontawesome import icons as fai

from louzlib.sty import get_orlog_fmt

logging.addLevelName(logging.DEBUG, f"d")
logging.addLevelName(logging.INFO, f"i")
logging.addLevelName(logging.WARNING, f"w")
logging.addLevelName(logging.ERROR, f"e")
logging.addLevelName(logging.NOTSET, f"n")
logging.addLevelName(logging.CRITICAL, f"c")


def get_logger(level: int = logging.DEBUG, app: str = "default") -> Logger:
    logr = logging.getLogger(app)
    logr.setLevel(level)
    return logr


def get_handler(level: int = logging.DEBUG) -> StreamHandler:
    handlr = StreamHandler(sys.stdout)
    handlr.setLevel(level)
    return handlr


def init_logger(level: int = logging.DEBUG, app: str = "default"):
    log4, handlr = get_logger(level, app), get_handler(level)

    fmt = logging.Formatter(
        get_orlog_fmt() | "[%(asctime)s - %(name)s - %(levelname)s] %(message)s",
        # Imagine if we could render a clock from  3 svgs just in time lol
        "%Y-%m-%d %H:%M:%S",
    )

    handlr.setFormatter(fmt)
    log4.addHandler(handlr)
    return log4
