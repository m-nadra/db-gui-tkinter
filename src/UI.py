from tkinter import Frame, LEFT, TOP, RIGHT, BOTTOM, BOTH
from tkinter import ttk


class MainWindowLayout:
    def __init__(self, root):
        self.header = Header(root)
        self.table = Table(root)
        self.options = Options(root)

    def getComponents(self):
        return self.header, self.table, self.options


class Header(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(anchor='ne', padx=50, pady=10)

        ttk.Label(self, text='Table:').pack(side=LEFT)
        self.combobox = ttk.Combobox(self)
        self.combobox.pack(side=RIGHT, fill=BOTH)


class Table(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=TOP, fill=BOTH, expand=True, padx=50, pady=10)

        self.tree = ttk.Treeview(self, show='headings')
        self.tree.pack(expand=True, fill=BOTH)


class Options(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text='Options')
        self.pack(side=BOTTOM, padx=50, pady=50, ipady=10)

        self.addButton = ttk.Button(self, text='Add')
        self.addButton.pack(side=LEFT, padx=10)
        self.editButton = ttk.Button(self, text='Edit')
        self.editButton.pack(side=LEFT, padx=10)
        self.deleteButton = ttk.Button(self, text='Delete')
        self.deleteButton.pack(side=LEFT, padx=10)
