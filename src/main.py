from tkinter import *
from tkinter import ttk
import queries
from table import TableContent, RecordManager

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("School Manager")
        self.geometry("800x600")

        self.header = Header(self)
        self.table = Table(self)
        self.tableContent = TableContent(self.header, self.table)
        self.recordManager = RecordManager(self.header, self.table)
        self.options = Options(self, self.tableContent, self.recordManager)


class Header(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(anchor='ne', padx=50, pady=10)
        ttk.Label(self, text='Table:').pack(side=LEFT)
        self.combobox = ttk.Combobox(self, values=queries.getTablesNames())
        self.combobox.pack(side=RIGHT, fill=BOTH)
        self.combobox.bind("<<ComboboxSelected>>", lambda _: parent.tableContent.updateTable())


class Table(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=TOP, fill=BOTH, expand=True, padx=50, pady=10)
        self.tree = ttk.Treeview(self, show='headings')
        self.tree.pack(expand=True, fill=BOTH)

    def refreshTable(self, columns, records):
        try:
            self.tree.destroy()
        except AttributeError:
            pass

        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        for column in columns:
            self.tree.heading(column, text=column)

        for row in records:
            self.tree.insert('', 'end', values=[column for column in row])

        self.tree.pack(expand=True, fill=BOTH)


class Options(ttk.LabelFrame):
    def __init__(self, parent, tableContent, recordManager):
        super().__init__(parent, text='Options')
        self.tableContent = tableContent
        self.recordManager = recordManager
        self.pack(side=BOTTOM, padx=50, pady=50, ipady=10)

        ttk.Button(self, text='Add', command=self.recordManager.addRecord).pack(side=LEFT, padx=10)
        ttk.Button(self, text='Edit', command=self.recordManager.editRecord).pack(side=LEFT, padx=10)
        ttk.Button(self, text='Delete', command=self.recordManager.deleteRecord).pack(side=LEFT, padx=10)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
