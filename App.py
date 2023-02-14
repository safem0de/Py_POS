import tkinter as tk

# Importing Tkinter module
from tkinter import *
from tkinter.ttk import *

from _Views.Main_view import View


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Py_POS powered by Safem0de')
        self.geometry('+10+10')

        # create a view and place it on the root window
        view = View(self)
        view.pack(fill = BOTH, expand = True)


if __name__ == '__main__':
    app = App()
    app.mainloop()