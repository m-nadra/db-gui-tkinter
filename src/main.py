from tkinter import Tk
from UI import MainWindowLayout
from logic import MainWindowLogic


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("School Manager")
        self.geometry("800x600")

        self.layout = MainWindowLayout(self)
        header, table, options = self.layout.getComponents()

        self.logic = MainWindowLogic(header, table)

        options.addButton['command'] = self.logic.addRecord
        options.editButton['command'] = self.logic.editRecord
        options.deleteButton['command'] = self.logic.deleteRecord


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
