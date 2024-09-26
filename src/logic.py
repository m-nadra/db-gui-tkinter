import queries
from windows import AddWindow
from tkinter import messagebox


class MainWindowLogic:
    def __init__(self, header, table):
        self.tableFrame = table
        self.tableContent = TableContent(table.tree)
        self.tableSelector = TableSelector(header.combobox, self.tableContent)

    def addRecord(self):
        tableName = self.tableContent.tableName
        addWindow = AddWindow(tableName)
        self.tableFrame.wait_window(addWindow)
        self.tableContent.updateTable(tableName)

    def editRecord(self):
        pass

    def deleteRecord(self):
        try:
            recordId = self.tableContent.tree.item(
                self.tableContent.tree.selection())['values'][0]
        except IndexError:
            messagebox.showerror("Error", "No record selected")
            return

        result = messagebox.askquestion(
            "Confirm deletion", "Do you want to remove the record?")
        if result == 'no':
            return

        tableName = self.tableContent.tableName
        tableClass = getattr(queries, tableName, None)
        if tableClass:
            tableClass.deleteRecord(recordId)

        self.tableContent.updateTable(tableName)


class TableContent:
    def __init__(self, tree):
        self.tree = tree
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


class TableSelector:
    def __init__(self, combobox, tableContent):
        self.combobox = combobox
        self.combobox['values'] = queries.getTablesNames()
        self.combobox.bind("<<ComboboxSelected>>",
                           lambda _: tableContent.updateTable(self.combobox.get()))
