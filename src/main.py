from tkinter import Tk, Frame, LEFT, TOP, RIGHT, BOTTOM, BOTH
from tkinter import ttk
import queries
from table import TableContent, TableSelector
from records_operations import AddRecord, EditRecord, DeleteRecord


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("School Manager")
        self.geometry("800x600")

        self.header = Header(self)
        self.table = Table(self)
        self.options = Options(self)
        self.tableContent = TableContent(self.table)
        self.tableSelector = TableSelector(
            self.header.combobox, self.tableContent)

    def addRecord(self):
        AddRecord(self.tableContent).execute()

    def editRecord(self):
        EditRecord(self.tableContent).execute()

    def deleteRecord(self):
        DeleteRecord(self.tableContent).execute()


class Header(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(anchor='ne', padx=50, pady=10)

        ttk.Label(self, text='Table:').pack(side=LEFT)
        self.combobox = ttk.Combobox(self, values=queries.getTablesNames())
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

        ttk.Button(self, text='Add', command=parent.addRecord).pack(
            side=LEFT, padx=10)
        ttk.Button(self, text='Edit', command=parent.editRecord).pack(
            side=LEFT, padx=10)
        ttk.Button(self, text='Delete', command=parent.deleteRecord).pack(
            side=LEFT, padx=10)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
