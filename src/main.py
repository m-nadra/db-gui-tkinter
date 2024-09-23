from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from add import AddWindow
import queries


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


class TableContent:
    def __init__(self, header, table):
        self.header = header
        self.table = table

    def updateTable(self):
        tableName = self.header.combobox.get()
        tableClass = getattr(queries, tableName, None)
        
        records = tableClass.get()
        columns = tableClass.getColumnNames()

        self.table.refreshTable(columns, records)


class RecordManager:
    def __init__(self, header, table):
        self.header = header
        self.table = table

    def addRecord(self):
        AddWindow(self.header.combobox.get())

    def deleteRecord(self):
        try:
            recordId = self.table.tree.item(self.table.tree.selection())['values'][0]
        except IndexError:
            messagebox.showerror("Error", "No record selected")
            return

        result = messagebox.askquestion("Confirm deletion", "Do you want to remove the record?")
        if result == 'no':
            return

        tableName = self.header.combobox.get()
        tableClass = getattr(queries, tableName, None)
        if tableClass:
            tableClass.deleteRecord(recordId)

    def editRecord(self):
        pass


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
