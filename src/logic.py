import queries
from records_operations import AddRecord, EditRecord, DeleteRecord


class MainWindowLogic:
    def __init__(self, header, table):
        self.tableContent = TableContent(table)
        self.tableSelector = TableSelector(header.combobox, self.tableContent)

    def addRecord(self):
        AddRecord(self.tableContent).execute()

    def editRecord(self):
        EditRecord(self.tableContent).execute()

    def deleteRecord(self):
        DeleteRecord(self.tableContent).execute()


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


class TableSelector:
    def __init__(self, combobox, tableContent):
        self.combobox = combobox
        self.combobox['values'] = queries.getTablesNames()
        self.tableContent = tableContent
        self.combobox.bind("<<ComboboxSelected>>",
                           lambda _: self.tableContent.updateTable(self.combobox.get()))
