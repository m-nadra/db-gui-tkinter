"""This module contains the classes that define the layout of the main window."""

from tkinter import Frame, LEFT, TOP, RIGHT, BOTTOM, BOTH
from tkinter import ttk


class MainWindowLayout:
    """Creates frames and widgets for the main window."""

    def __init__(self, parentWindow):
        parentWindow.title("School Manager")
        parentWindow.geometry("800x600")
        self.header = Header(parentWindow)
        self.table = Table(parentWindow)
        self.options = Options(parentWindow)

    def getComponents(self) -> tuple:
        """Returns the components of the main window."""
        return self.header, self.table, self.options


class Header(Frame):
    """Header frame with a combobox to select the table."""

    def __init__(self, parentWindow):
        super().__init__(parentWindow)
        self.pack(anchor='ne', padx=50, pady=10)

        ttk.Label(self, text='Table:').pack(side=LEFT)
        self.combobox = ttk.Combobox(self)
        self.combobox.pack(side=RIGHT, fill=BOTH)


class Table(Frame):
    """Table frame with a table to display the records."""

    def __init__(self, parentWindow):
        super().__init__(parentWindow)
        self.pack(side=TOP, fill=BOTH, expand=True, padx=50, pady=10)

        self.table = ttk.Treeview(self, show='headings')
        self.table.pack(expand=True, fill=BOTH)


class Options(ttk.LabelFrame):
    """Options frame with buttons to add, edit, and delete records."""

    def __init__(self, parentWindow):
        super().__init__(parentWindow, text='Options')
        self.pack(side=BOTTOM, padx=50, pady=50, ipady=10)

        self.addButton = ttk.Button(self, text='Add')
        self.addButton.pack(side=LEFT, padx=10)

        self.editButton = ttk.Button(self, text='Edit')
        self.editButton.pack(side=LEFT, padx=10)

        self.deleteButton = ttk.Button(self, text='Delete')
        self.deleteButton.pack(side=LEFT, padx=10)
