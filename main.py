# coding=UTF-8
import logging
import logging.handlers

log_dict_conf = __import__("dict_config")
logger = logging.getLogger(f'main.{__name__}')

from body.controller import Controllers
if __name__ == '__main__':
    logger.debug('Start program')
    try:
        Controllers().show_main_window()
    except Exception:
        logger.exception("Error when starting the main program window")
    logger.debug('Stop program')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
