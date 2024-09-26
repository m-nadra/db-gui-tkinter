"""This module contains the classes to manipulate data in widgets."""

from windows import AddWindow
from tkinter import messagebox
import queries


class MainWindowLogic:
    """Create the logic for the main window."""

    def __init__(self, headerFrame, tableFrame):
        self.tableFrame = tableFrame
        self.tableContent = TableContent(tableFrame.table)
        self.tableSelector = TableSelector(
            headerFrame.combobox, self.tableContent)

    def addRecord(self) -> None:
        """Create a window with form to add a record. After adding the record, update the table widget."""
        tableName = self.tableContent.getTableName()
        addWindow = AddWindow(tableName)
        self.tableFrame.wait_window(addWindow)
        self.tableContent.updateTable(tableName)

    def editRecord(self):
        pass

    def deleteRecord(self) -> None:
        """Delete the selected record. After deleting the record, update the table widget."""
        try:
            recordId = self.tableContent.getSelectedRecord()
        except IndexError:
            messagebox.showerror("Error", "No record selected")
            return

        userConfirmation = messagebox.askquestion(
            "Confirm deletion", "Do you want to remove the record?")
        if userConfirmation == 'no':
            return

        tableName = self.tableContent.getTableName()
        tableClass = getattr(queries, tableName, None)
        tableClass.deleteRecord(recordId)
        self.tableContent.updateTable(tableName)


class TableContent:
    """Manage the content of the table widget."""

    def __init__(self, tableWidget):
        self.tableWidget = tableWidget
        self.tableName: str
        self.rows: list
        self.columnNames: list

    def updateTable(self, tableName: str) -> None:
        """Update object attributes and refresh the table widget."""
        self.tableName = tableName
        tableClass = getattr(queries, tableName, None)
        self.rows = tableClass.getRows()
        self.columnNames = tableClass.getColumnNames()
        self.refreshTable()

    def refreshTable(self) -> None:
        """Delete all the records in the table widget and insert the new records."""
        self.clearTableWidget()

        self.tableWidget["columns"] = self.columnNames

        for column in self.columnNames:
            self.tableWidget.heading(column, text=column)
            self.tableWidget.column(column, width=100)

        for row in self.rows:
            self.tableWidget.insert(
                '', 'end', values=[column for column in row])

    def getTableName(self) -> str:
        """Return the name of the dispaled table."""
        return self.tableName

    def getSelectedRecord(self) -> int:
        """Return the id of the selected record"""
        return self.tableWidget.item(self.tableWidget.selection())['values'][0]

    def clearTableWidget(self) -> None:
        """Remove all the records in the table widget"""
        for col in self.tableWidget.get_children():
            self.tableWidget.delete(col)


class TableSelector:
    """Manage the table selection combobox."""

    def __init__(self, combobox, tableContent):
        self.combobox = combobox
        self.combobox['values'] = queries.getTablesNames()
        self.combobox.bind("<<ComboboxSelected>>",
                           lambda _: tableContent.updateTable(self.combobox.get()))
