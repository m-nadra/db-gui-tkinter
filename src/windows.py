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
