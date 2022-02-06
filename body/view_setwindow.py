import tkinter as tk
import logging

logger = logging.getLogger('main.' + __name__)


def setwindow(root):
    root.title('window of program')
    root.resizable(False, False)
    w = 800
    h = 600
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = int(ws / 2 - w / 2)
    y = int(hs / 2 - h / 2)
    root.geometry('{0}x{1}+{2}+{3}'.format(w, h, x, y))
    logger.debug('"setwindow" worked')
