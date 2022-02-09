# coding=UTF-8
import tkinter as tk
from body.list_goods import list_goods
import body.view_interface as interfase
import logging

logger = logging.getLogger('main.' + __name__)


class ViewForGood:
    """Describe view for goods"""

    def __init__(self):
        self.list_goods = []
        self.output_list_goods = []

    @staticmethod
    def data_from_list():
        """Create a file and enter the data from the list into it"""
        with open('body/goods.info', 'w', encoding='utf-8') as goods:
            for line in list_goods:
                goods.write(line)

        logger.debug('Data file "goods.info" is created')

    def data_from_file(self):
        """Create a list of data to enter it into the database"""
        with open('body/goods.info', 'r', encoding='utf-8') as goods:
            for line in goods.readlines():
                self.list_good = line.split(':')
                self.output_list_goods.append([self.list_good[0], int(self.list_good[1]), int(self.list_good[2])])

        logger.debug('A list with data to be entered into the database has been created')

        return self.output_list_goods

    @staticmethod
    def start_main_window():
        """Function of initiating the main window of the program."""
        root = tk.Tk()
        root.title('Работаем с БД')
        root.resizable(False, False)
        w = 800
        h = 600
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = int(ws / 2 - w / 2)
        y = int(hs / 2 - h / 2)
        root.geometry('{0}x{1}+{2}+{3}'.format(w, h, x, y))
        # raise ValueError('Test error')
        interfase.MainWindow(root)
        root.mainloop()
