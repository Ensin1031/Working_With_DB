# coding=UTF-8
import logging
import logging.handlers

log_dict_conf = __import__("dictConfig")
logger = logging.getLogger('main.' + __name__)

from body.controller import show_main_window

if __name__ == '__main__':
    logger.debug('Start program')
    try:

        show_main_window()
    except Exception:
        logger.exception("Error when starting the main program window")
    logger.debug('Stop program')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
