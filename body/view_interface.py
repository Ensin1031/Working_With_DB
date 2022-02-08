# coding=UTF-8
import tkinter as tk
from body.view_setwindow import setwindow
from functools import partial
from body.model import create_good_from_list, delete_goods_from_list
import body.controller as cont

import logging
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
        for child in event.widget.children.values():  # change color of child widgets too
            child.config(bg=color)

    def __color_button(self, button, color_e, color_l):
        button.bind('<Enter>', partial(self.__color_event_bg, button, color_e))
        button.bind('<Leave>', partial(self.__color_event_bg, button, color_l))

    def __on_mousewheel(self, event):
        """Function to scroll the result window with the mouse wheel"""
        self.canvas.yview_scroll(-1 * int(event.delta / 120), "units")
        return 'break'

    def __enter_data(self):
        """Enter initial date in DB"""
        cont.primary_data()
        self.lable_exit.config(text='Первоначальные данные в базу былы добавлены')
        logger.debug('MainWindow.__enter_data. Initial data has been added to the database.')
        self.__output_frame(cont.result_list())

    def __enter_user_data(self):
        """Function for adding users data"""
        try:
            user_data_list = [self.add_enter_name.get(), int(self.add_enter_price.get()),
                              int(self.add_enter_count.get())]
        except Exception:
            self.lable_exit.config(text='Введите корректные данные: price и count должны иметь числовые значения')
            logger.exception('Wrong type of data entered')
        else:
            create_good_from_list(user_data_list)
            self.lable_exit.config(text=f'Ваш продукт "{user_data_list[0]}" добавлен в таблицу')
        self.__output_frame(cont.result_list())

    def __del_by_name(self):
        """A function to delete data from a table by name."""
        data = self.add_deleting_name.get()
        resp = delete_goods_from_list(data)
        if resp:
            self.lable_exit.config(text=f'Продукт с именем "{data}" удален из таблицы')
        else:
            self.lable_exit.config(text=f'Продукт с именем "{data}" отсутствует в таблице')
        self.__output_frame(cont.result_list())

    def __max_min_values(self):
        """Function of max and min values"""
        data = cont.max_min_func()
        if data == False:
            self.lable_exit.config(text='БД пуста, откуда тут возьмутся максимальные или минимальные значения?!')
        else:
            self.lable_exit.config(text=f'Максимальное значение поля "цена" = "{data[0]}", минимальное = "{data[1]}"')
            self.__output_frame(data[2])

    def __clean_db(self):
        """Function of completely deleting data from the database."""
        if cont.clear_db_func():
            self.lable_exit.config(text='БД теперь полностью пуста.')
        else:
            self.lable_exit.config(text='БД и так полностью пуста, хватит баловаться...')
        self.__output_frame(cont.result_list())

    def json_in_file(self):
        """Function of outputting data from the database to a file in JSON format"""
        data = cont.json_output()
        if data:
            self.lable_exit.config(text=f'БД записана в JSON формате в файл "{data}"')
            self.__output_frame(cont.result_list())
        else:
            self.lable_exit.config(text='БД пуста. Нечего выводить в файл....')
            self.__output_frame(cont.result_list())

    def __init_window(self):
        """Main window"""
        setwindow(self.root)
        self.root.title('Работаем с БД')
        # create frames
        self.user_frame = tk.Frame(self.root, width=785, height=147).place(relx=0.01, rely=0.001)
        self.result_frame = tk.Frame(self.root, width=785, height=430)
        # adding initial data
        tk.Label(self.user_frame,
                 text='Создаем таблицу "goods" в БД и вносим в нее первоначальные данные:',
                 font='Arial 12'
                 ).place(relx=0.05, rely=0.002)  # initial data entry mark
        self.enter_button = tk.Button(self.user_frame, font='Arial 8', bg='#f0f0f0',
                                      text='ENTER', command=self.__enter_data)  # Button for adding initial data.
        # adding user data
        tk.Label(self.user_frame,
                 text='Добавьте в таблицу свой продукт:',
                 font='Arial 12'
                 ).place(relx=0.05, rely=0.044)
        self.add_button = tk.Button(self.user_frame, font='Arial 8', bg='#f0f0f0',
                                    text='INPUT', command=self.__enter_user_data)  # Button for adding users data.
        # input fields for user data
        self.add_enter_name = tk.Entry(self.user_frame, font='Arial 12', width=20)
        self.add_enter_name.insert(tk.END, 'имя')
        self.add_enter_price = tk.Entry(self.user_frame, font='Arial 12', width=7)
        self.add_enter_price.insert(tk.END, 'цена')
        self.add_enter_count = tk.Entry(self.user_frame, font='Arial 12', width=7)
        self.add_enter_count.insert(tk.END, 'кол-во')
        # deleting data by name
        tk.Label(self.user_frame,
                 text='Удалите запись из таблицы по имени:',
                 font='Arial 12'
                 ).place(relx=0.05, rely=0.085)
        self.del_button = tk.Button(self.user_frame, font='Arial 8', bg='#f0f0f0',
                                    text='DELETE', command=self.__del_by_name)  # Button for deleting data by nane.
        # input fields for user data
        self.add_deleting_name = tk.Entry(self.user_frame, font='Arial 12', width=20)
        self.add_deleting_name.insert(tk.END, 'имя')
        # outpum max. and min. date
        tk.Label(self.user_frame,
                 text='Выведите данные по макс. и мин. значениям поля "цена":',
                 font='Arial 12'
                 ).place(relx=0.05, rely=0.126)
        self.max_min_button = tk.Button(self.user_frame, font='Arial 8', bg='#f0f0f0',
                                        text='MAX/MIN',
                                        command=self.__max_min_values)  # Button for output max/man data.
        # clear DB
        self.clear_db_button = tk.Button(self.user_frame, font='Arial 10', bg='red',
                                         text='Полное удаление данных из БД', command=self.__clean_db)
        # data output to json file
        self.json_button = tk.Button(self.user_frame, font='Arial 10', bg='#f0f0f0',
                                     text='Вывод данных в JSON файл', command=self.json_in_file)

        self.lable_exit = tk.Label(self.user_frame, font='Arial 12',
                                   text='Не нажимайте красную кнопку!')  # label of messages to the user
        # bind fields to the <ENTER> key
        self.add_enter_name.bind('<Return>', partial(self.__enter_user_data))
        self.add_enter_price.bind('<Return>', partial(self.__enter_user_data))
        self.add_enter_count.bind('<Return>', partial(self.__enter_user_data))
        self.add_deleting_name.bind('<Return>', partial(self.__del_by_name))

        self.__color_button(self.enter_button, 'white', '#f0f0f0')
        self.__color_button(self.add_button, 'white', '#f0f0f0')
        self.__color_button(self.del_button, 'white', '#f0f0f0')
        self.__color_button(self.max_min_button, 'white', '#f0f0f0')
        self.__color_button(self.clear_db_button, 'green', 'red')
        self.__color_button(self.json_button, 'white', '#f0f0f0')

        self.add_enter_name.place(relx=0.4, rely=0.045)
        self.add_enter_price.place(relx=0.64, rely=0.043)
        self.add_enter_count.place(relx=0.73, rely=0.045)
        self.add_deleting_name.place(relx=0.5, rely=0.086)

        self.enter_button.place(relx=0.85, rely=0.002)
        self.add_button.place(relx=0.85, rely=0.043)
        self.del_button.place(relx=0.85, rely=0.085)
        self.max_min_button.place(relx=0.85, rely=0.126)
        self.clear_db_button.place(relx=0.05, rely=0.176)
        self.json_button.place(relx=0.32, rely=0.176)

        self.lable_exit.place(relx=0.5, rely=0.25, anchor='center')
        self.result_frame.place(relx=0.01, rely=0.27)

    def __output_frame(self, args):
        """Creating a content list and processing it."""

        # Cleaning content from old results.
        result_frame_plase_list = self.result_frame.place_slaves()
        result_frame_pack_list = self.result_frame.pack_slaves()

        if len(result_frame_plase_list) > 0:
            for value in result_frame_plase_list:
                value.destroy()
        if len(result_frame_pack_list) > 0:
            for value in result_frame_pack_list:
                value.destroy()

        # frame height
        height_scroll = (1 + len(args)) * 21

        # enter canvas
        self.canvas = tk.Canvas(self.result_frame,
                                width=785,
                                height=420,
                                scrollregion=(0, 0, 785, height_scroll))

        if 1 < len(args) <= 21:
            self.frame_str = tk.Frame(self.result_frame, width=785, height=430)

            self.__output_list(args)

            self.frame_str.pack()

        else:
            # scrollbar
            sbar = tk.Scrollbar(self.result_frame, command=self.canvas.yview)
            self.canvas.config(yscrollcommand=sbar.set)
            self.canvas.bind_all("<MouseWheel>", self.__on_mousewheel)
            sbar.place(relx=1, rely=1, anchor='se', relheight=1)
            self.canvas.pack()

            # internal frames
            inner_frame = tk.Frame(self.canvas, width=785, height=height_scroll)
            self.canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

            self.frame_str = tk.Frame(inner_frame, width=785, height=430)

            self.__output_list(args)

            self.frame_str.pack()

    def __output_list(self, args):
        """Final data output."""
        if len(args) > 0:
            frame_header = tk.Frame(self.frame_str, width=785, height=21)
            frame_header.pack()
            tk.Label(frame_header, font='Tahoma 9', text='Название продукта').place(relx=0.01, rely=0)
            tk.Label(frame_header, font='Tahoma 9', text='Цена').place(relx=0.6, rely=0)
            tk.Label(frame_header, font='Tahoma 9', text='Количество').place(relx=0.97, rely=0, anchor='ne')

        for row in args:
            self.frame = tk.Frame(self.frame_str, width=785, height=21)
            self.ln = tk.Label(self.frame, font='Tahoma 9', text=row[0])
            self.ls = tk.Label(self.frame, font='Tahoma 9', text=row[1])
            self.ld = tk.Label(self.frame, font='Tahoma 9', text=row[2])

            self.__color_button(self.frame, 'white', '#f0f0f0')

            self.frame.pack()
            self.ln.place(relx=0.01, rely=0)
            self.ls.place(relx=0.6, rely=0, anchor='ne')
            self.ld.place(relx=0.97, rely=0, anchor='ne')


def start_main_window():
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    start_main_window()
