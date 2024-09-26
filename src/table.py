from tkinter import messagebox
from windows import AddWindow
import queries


class TableContent:
    def __init__(self, table):
        self.frame = table
        self.tree = table.tree
        self.tableName = ""
        self.columns = []
        self.rows = []

    def updateTable(self, tableName):
        self.tableName = tableName
        tableClass = getattr(queries, tableName, None)
        self.records = tableClass.get()
        self.columns = tableClass.getColumnNames()
        self.refreshTable()

    def refreshTable(self):
        for col in self.tree.get_children():
            self.tree.delete(col)

        self.tree["columns"] = self.columns

        for column in self.columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=100)

        for row in self.records:
            self.tree.insert('', 'end', values=[column for column in row])


class RecordManager:
    def __init__(self, table):
        self.table = table
        self.frame = self.table.frame

    def addRecord(self):
        tableName = self.table.tableName
        addWindow = AddWindow(tableName)
        self.frame.wait_window(addWindow)
        self.table.updateTable(tableName)

    def deleteRecord(self):
        try:
            recordId = self.table.tree.item(
                self.table.tree.selection())['values'][0]
        except IndexError:
            messagebox.showerror("Error", "No record selected")
            return

        result = messagebox.askquestion(
            "Confirm deletion", "Do you want to remove the record?")
        if result == 'no':
            return

        tableName = self.table.tableName
        tableClass = getattr(queries, tableName, None)
        if tableClass:
            tableClass.deleteRecord(recordId)

        self.table.updateTable(tableName)

    def editRecord(self):
        pass


class TableSelector:
    def __init__(self, combobox, tableContent):
        self.combobox = combobox
        self.tableContent = tableContent
        self.combobox.bind("<<ComboboxSelected>>",
                           lambda _: self.tableContent.updateTable(self.combobox.get()))
