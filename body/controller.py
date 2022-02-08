# coding=UTF-8
from body.model import create_good_from_list, show_the_entire_list, clean_db, max_min_goods_on_the_list, db_in_json
from os import listdir
from body.view_interface import start_main_window
from body.view import ViewForGood
import logging

logger = logging.getLogger('main.' + __name__)

def primary_data():
    """Entering initial data into the database."""
    for row in ViewForGood().data_from_file():
        create_good_from_list(row)

    logger.info('The data has been entered into the database.')

def show_main_window():
    """The function of obtaining the initial data file for the database and launching the main user window."""
    ViewForGood().data_from_list()
    start_main_window()


def result_list():
    """The function of passing the database content sheet to the output in Tkinter"""
    return show_the_entire_list()


def max_min_func():
    """Function of initial processing of max and min values."""
    data = max_min_goods_on_the_list()

    if len(data[2]) == 2 and data[2][0][0] == data[2][1][0]:
        return [data[0], data[1], [data[2][0]], True]
    elif data[2]:
        data.append(True)
        return data
    else:
        return False


def clear_db_func():
    """Function of completely deleting data from the database."""
    if show_the_entire_list():
        clean_db()
        logger.info('DB is cleaned')
        return True
    else:
        return False


def json_output():
    """Function of outputting data from the database to a file in JSON format"""
    file_way = 'json_files/{0}_db_in_json.json'.format(len(listdir(path='json_files')))
    if show_the_entire_list():
        db_in_json(file_way)
        logger.info(f'The database is written in JSON format to the file "{file_way}"')
        return file_way
    else:
        logger.info('DB is empty, unsuccessful attempt to create JSON file')
        return False
