from tkinter import messagebox
from windows import AddWindow
import queries

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
        addWindow = AddWindow(self.header.combobox.get())
        self.header.wait_window(addWindow)
        self.updateTable()
        
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

        self.updateTable()

    def updateTable(self):
        tableName = self.header.combobox.get()
        tableClass = getattr(queries, tableName, None)
        
        records = tableClass.get()
        columns = tableClass.getColumnNames()

        self.table.refreshTable(columns, records)

    def editRecord(self):
        pass

