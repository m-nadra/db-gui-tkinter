"""This module is the entry point of the application. It creates the main window and connects the logic and layout."""

from tkinter import Tk
from UI import MainWindowLayout
from logic import MainWindowLogic


class MainWindow(Tk):
    """This class is an connection between the layout and the logic of the main window."""

    def __init__(self):
        super().__init__()
        self.layout = MainWindowLayout(self)
        header, table, options = self.layout.getComponents()
        self.logic = MainWindowLogic(header, table)

        options.addButton['command'] = self.logic.addRecord
        options.editButton['command'] = self.logic.editRecord
        options.deleteButton['command'] = self.logic.deleteRecord


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
