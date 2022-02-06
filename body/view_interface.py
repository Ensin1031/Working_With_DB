import tkinter as tk
from functools import partial
import logging
from body.view_setwindow import setwindow
from body.controller import primary_data
from body.model import create_good_from_list, delete_goods_from_list

logger = logging.getLogger('main.' + __name__)


class MainWindow(tk.Frame):
    """Main user interface class"""
    logger.debug('MainWindow. Launch tkinter MainWindows')

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.__init_window()

    @staticmethod
    def __color_event_bg(widget, color, event):
        """Function of changing the color of the field on an event"""
        event.widget.config(bg=color)
        for child in event.widget.children.values():    # change color of child widgets too
            child.config(bg=color)

    def __enter_data(self):
        primary_data()
        self.lable_exit.config(text='Первоначальные данные в базу былы добавлены')
        logger.debug('MainWindow.__enter_data. Initial data has been added to the database.')

    def __enter_user_data(self):
        """Function for adding users data"""
        try:
            user_data_list = [self.add_enter_name.get(), int(self.add_enter_price.get()), int(self.add_enter_count.get())]
        except Exception:
            self.lable_exit.config(text='Введите корректные данные: price и count должны иметь числовые значения')
            logger.exception('Wrong type of data entered')
        else:
            create_good_from_list(user_data_list)
            self.lable_exit.config(text=f'Ваш продукт "{user_data_list[0]}" добавлен в таблицу')

    def __del_by_name(self):
        """A function to delete data from a table by name."""
        data = self.add_deleting_name.get()
        resp = delete_goods_from_list(data)
        if resp == True:
            self.lable_exit.config(text=f'Продукт с именем "{data}" удален из таблицы')
        else:
            self.lable_exit.config(text=f'Продукт с именем "{data}" отсутствует в таблице')

    def __init_window(self):
        """Main window"""
        setwindow(self.root)
        self.root.title('Работаем с БД')
        # create frames
        self.user_frame = tk.Frame(self.root, width=785, height=147, bg='red').place(relx=0.01, rely=0.001)
        self.result_frame = tk.Frame(self.root, width=785, height=430, bg='yellow')
        # adding initial data
        tk.Label(self.user_frame,
                 text='Создаем таблицу "goods" в БД и вносим в нее первоначальные данные:',
                 font='Arial 14'
                 ).place(relx=0.02, rely=0.002)  # initial data entry mark
        self.enter_button = tk.Button(self.user_frame, font='Arial 11', bg='#f0f0f0',
                                       text='ENTER', command=self.__enter_data)     # Button for adding initial data.
        # adding user data
        tk.Label(self.user_frame,
                 text='Добавьте в таблицу свой продукт:',
                 font='Arial 14'
                 ).place(relx=0.02, rely=0.05)  # initial data entry mark
        self.add_button = tk.Button(self.user_frame, font='Arial 11', bg='#f0f0f0',
                                       text='INPUT', command=self.__enter_user_data)     # Button for adding initial data.
        # input fields for user data
        self.add_enter_name = tk.Entry(self.user_frame, font='Arial 12', width=20)
        self.add_enter_name.insert(tk.END, 'name')
        self.add_enter_price = tk.Entry(self.user_frame, font='Arial 12', width=7)
        self.add_enter_price.insert(tk.END, 'price')
        self.add_enter_count = tk.Entry(self.user_frame, font='Arial 12', width=7)
        self.add_enter_count.insert(tk.END, 'count')

        # deleting data by name
        tk.Label(self.user_frame,
                 text='Удалите запись из таблицы по имени:',
                 font='Arial 14'
                 ).place(relx=0.02, rely=0.1)  # initial data entry mark
        self.del_button = tk.Button(self.user_frame, font='Arial 11', bg='#f0f0f0',
                                       text='DELETE', command=self.__del_by_name)     # Button for deleting initial data.
        # input fields for user data
        self.add_deleting_name = tk.Entry(self.user_frame, font='Arial 12', width=20)
        self.add_deleting_name.insert(tk.END, 'name')


        self.lable_exit = tk.Label(self.user_frame, font='Arial 12', text='')  # label of messages to the user

        self.add_enter_name.bind('<Return>', partial(self.__enter_user_data))  # биндим поле на клавишу <Enter>
        self.add_enter_price.bind('<Return>', partial(self.__enter_user_data))  # биндим поле на клавишу <Enter>
        self.add_enter_count.bind('<Return>', partial(self.__enter_user_data))  # биндим поле на клавишу <Enter>
        self.add_deleting_name.bind('<Return>', partial(self.__del_by_name))  # биндим поле на клавишу <Enter>

        self.enter_button.bind('<Enter>', partial(self.__color_event_bg, self.enter_button, '#B7EFF0'))
        self.enter_button.bind('<Leave>', partial(self.__color_event_bg, self.enter_button, '#f0f0f0'))

        self.add_button.bind('<Enter>', partial(self.__color_event_bg, self.add_button, '#B7EFF0'))
        self.add_button.bind('<Leave>', partial(self.__color_event_bg, self.add_button, '#f0f0f0'))

        self.del_button.bind('<Enter>', partial(self.__color_event_bg, self.add_button, '#B7EFF0'))
        self.del_button.bind('<Leave>', partial(self.__color_event_bg, self.add_button, '#f0f0f0'))

        self.add_enter_name.place(relx=0.4, rely=0.055)
        self.add_enter_price.place(relx=0.64, rely=0.055)
        self.add_enter_count.place(relx=0.73, rely=0.055)
        self.add_deleting_name.place(relx=0.5, rely=0.105)

        self.enter_button.place(relx=0.85, rely=0.002)
        self.add_button.place(relx=0.85, rely=0.05)
        self.del_button.place(relx=0.85, rely=0.1)
        self.lable_exit.place(relx=0.5, rely=0.23, anchor='center')

        self.result_frame.place(relx=0.01, rely=0.27)



def start_main_window():
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    start_main_window()