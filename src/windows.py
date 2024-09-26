"""This module contains classes to create additional windows."""

from tkinter import Toplevel
from tkinter import ttk
import queries


class AddWindow(Toplevel):
    """Create a window with a form to add a record to a table."""

    def __init__(self, tableName):
        super().__init__()
        self.title(f"Add record to {tableName}")
        self.geometry("400x300")
        self.tableName = tableName
        self.columns = getattr(queries, tableName).getColumnNames()[1:]
        self.entries = {}
        self.generateForm()

    def generateForm(self) -> None:
        """Generate widgets for the form."""
        for column in self.columns:
            ttk.Label(self, text=f'{column}:').pack()
            entry = ttk.Entry(self)
            entry.pack()
            self.entries[column] = entry
        ttk.Button(self, text='Add', command=self.addRecord).pack()

    def addRecord(self):
        """Add the record to the table. Destroy the window after adding the record."""
        data = {column: self.entries[column].get() for column in self.columns}
        tableClass = getattr(queries, self.tableName)
        tableClass.addRecord(**data)
        self.destroy()


class EditWindow(Toplevel):
    """Create a window with a form to edit a record in a table."""

    def __init__(self, tableName, recordId):
        super().__init__()
        self.title(f"Edit record in {tableName}")
        self.geometry("400x300")
        self.tableName = tableName
        self.columns = getattr(queries, tableName).getColumnNames()[1:]
        self.entries = {}
        self.recordId = recordId
        self.recordData = getattr(queries, tableName).getRecord(recordId)
        self.generateForm()

    def generateForm(self) -> None:
        """Generate widgets for the form."""
        for i, column in enumerate(self.columns, start=1):
            ttk.Label(self, text=f'{column}:').pack()
            entry = ttk.Entry(self)
            entry.pack()
            entry.insert(0, self.recordData[i])
            self.entries[column] = entry
        ttk.Button(self, text='Edit', command=self.editRecord).pack()

    def editRecord(self):
        """Edit the record in the table. Destroy the window after editing the record."""
        data = {column: self.entries[column].get() for column in self.columns}
        tableClass = getattr(queries, self.tableName)
        tableClass.updateRecord(self.recordId, **data)
        self.destroy()
