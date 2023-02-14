from tkinter import ttk
import tkinter as tk

class View(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        tabControl = ttk.Notebook(self)

        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)

        tabControl.add(tab1, text='จัดการรายการสินค้า')
        tabControl.add(tab2, text='ขายสินค้า')
        tabControl.add(tab3, text='รับสินค้า')

        tabControl.pack(expand=1, fill="both")

        self.ProductCode_label = ttk.Label(tab1, text='รหัสสินค้า :')
        self.ProductCode_label.grid(row=0, column=0, sticky=tk.NW)

        self.ProductCode_var = tk.StringVar()
        self.ProductCode_entry = ttk.Entry(tab1, textvariable=self.ProductCode_var, width=30)
        self.ProductCode_entry.grid(row=0, column=1)

        self.ProductName_label = ttk.Label(tab1, text='ชื่อสินค้า :')
        self.ProductName_label.grid(row=1, column=0, sticky=tk.NW)

        self.ProductName_var = tk.StringVar()
        self.ProductName_entry = ttk.Entry(tab1, textvariable=self.ProductName_var, width=30)
        self.ProductName_entry.grid(row=1, column=1)

        self.ProductPrice_label = ttk.Label(tab1, text='ราคา :')
        self.ProductPrice_label.grid(row=1, column=2, sticky=tk.NW)

        self.ProductPrice_var = tk.StringVar()
        self.ProductPrice_entry = ttk.Entry(tab1, textvariable=self.ProductPrice_var)
        self.ProductPrice_entry.grid(row=1, column=3)

        self.ProductUnit_label = ttk.Label(tab1, text='หน่วย :')
        self.ProductUnit_label.grid(row=1, column=4, sticky=tk.NW)

        self.ProductUnit_var = tk.StringVar()
        self.ProductUnit_combo = ttk.Combobox(tab1, textvariable=self.ProductUnit_var)
        self.ProductUnit_combo.grid(row=1, column=5)