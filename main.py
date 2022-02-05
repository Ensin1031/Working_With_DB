# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from body.model import primary_data,max_min_goods_on_the_list, max_min_log
import logging
import logging.handlers

def init_logger(name):
    logger = logging.getLogger(name)
    FORMAT = '%(asctime)s - %(name)s:%(lineno)s - %(levelname)s - %(message)s'
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter(FORMAT))
    stream_handler.setLevel(logging.DEBUG)
    file_handler = logging.handlers.RotatingFileHandler(filename="logs/test.log", maxBytes=10000, backupCount=10)
    file_handler.setFormatter(logging.Formatter(FORMAT))
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    logger.info("logger was initialized")


init_logger('app')
logger = logging.getLogger('app.main')

def make_work():

    conf = max_min_goods_on_the_list()
    print(conf)
    if conf:
        logger.debug(conf)
        try:
            logger.debug(max_min_log())
        except ValueError:
            logger.error('Error')


def main():
    primary_data()
    logger.debug('Start program')
    make_work()


if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
