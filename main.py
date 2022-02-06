# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# import logging
import logging.handlers

log_dict_conf = __import__("dictConfig")
logger = logging.getLogger('main.' + __name__)

from body.model import primary_data, max_min_goods_on_the_list, show_the_entire_list


def main():
    logger.debug('Start program')
    primary_data()
    max_min_goods_on_the_list()
    logger.debug('Stop program')


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
