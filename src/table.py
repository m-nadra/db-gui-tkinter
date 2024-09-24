from tkinter import messagebox
from windows import AddWindow
import queries

class TableContent:
    def __init__(self, table):
        self.tree = table.tree

    def updateTable(self, tableName):
        tableClass = getattr(queries, tableName, None)
        
        records = tableClass.get()
        columns = tableClass.getColumnNames()

        self.refreshTable(columns, records)

    def refreshTable(self, columns, records):
        for col in self.tree.get_children():
            self.tree.delete(col)

        self.tree["columns"] = columns
        
        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=100)

        for row in records:
            self.tree.insert('', 'end', values=[column for column in row])


class RecordManager:
    def __init__(self, header, table):
        self.header = header
        self.table = table

    def addRecord(self):
        tableName = self.header.combobox.get()
        addWindow = AddWindow(tableName)
        self.header.wait_window(addWindow)
        self.table.updateTable(tableName)
        
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

        self.table.updateTable(tableName)

    def editRecord(self):
        pass
