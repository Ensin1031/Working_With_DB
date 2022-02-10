# coding=UTF-8
import logging
from body.model import create_good_from_list, show_the_entire_list, max_min_goods_on_the_list
from body.model import delete_goods_from_list, db_in_json, clean_db
import body.view_file as view

logger = logging.getLogger(f'main.{__name__}')


class Controllers:
    """Single controller class."""

    @staticmethod
    def primary_data():
        """Entering initial data into the database."""
        for row in view.ViewForGood().data_from_file():
            create_good_from_list(row)

        logger.info('The data has been entered into the database.')

    @staticmethod
    def show_main_window():
        """The function of obtaining the initial data file for the database and launching the main user window."""
        logger.debug('Funktion show_main_window is worked')
        view.ViewForGood().data_from_list()
        view.ViewForGood().start_main_window()

    @staticmethod
    def create_user_good(data):
        """A function that creates products from a list."""
        logger.debug('Function create_user_good is worked')
        return create_good_from_list(data)

    @staticmethod
    def result_list():
        """The function of passing the database content sheet to the output in Tkinter"""
        return show_the_entire_list()

    @staticmethod
    def del_data(data):
        """Function to delete data by name."""
        deld = delete_goods_from_list(data)
        if deld:
            logger.debug(f'del_data is worked. Product "{data}" removed from the list')
            return deld

    @staticmethod
    def max_min_func():
        """Function of initial processing of max and min values."""
        data = max_min_goods_on_the_list()
        if data:
            return data
        return False

    @staticmethod
    def clear_db_func():
        """Function of completely deleting data from the database."""
        if show_the_entire_list():
            clean_db()
            logger.info('DB is cleaned')
            return True
        else:
            return False

    @staticmethod
    def json_output():
        """Function of outputting data from the database to a file in JSON format"""
        data = db_in_json()
        if data:
            logger.info(f'The database is written in JSON format to the file "{data}"')
            return data
        else:
            logger.info('DB is empty, unsuccessful attempt to create JSON file')
            return False
