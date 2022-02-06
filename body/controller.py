'''
связующее звено, принимающее запрос от пользователя, понимает,
какую модель он должен вызвать, чтобы получить какие то конкретные
данные, и, соответственно подключает нужный вид
'''

from body.view import ViewForGood
from body.model import create_good_from_list
import logging

logger = logging.getLogger('main.' + __name__)


def primary_data():
    ViewForGood().data_from_file()

    for row in ViewForGood().data_from_file():
        create_good_from_list(row)

    logger.info('The data has been entered into the database.')
