from tkinter import Toplevel
from tkinter import ttk
import queries


class AddWindow(Toplevel):
    def __init__(self, tableName):
        super().__init__()
        self.tableName = tableName
        self.title(f"Add record to {tableName}")
        self.geometry("400x300")

        self.columns = getattr(queries, tableName).getColumnNames()[1:]
        self.entries = {}
        self.generateForm()

    def generateForm(self):
        for column in self.columns:
            ttk.Label(self, text=f'{column}:').pack()
            entry = ttk.Entry(self)
            entry.pack()
            self.entries[column] = entry

        ttk.Button(self, text='Add', command=self.addRecord).pack()

    def addRecord(self):
        data = {column: self.entries[column].get() for column in self.columns}
        table_class = getattr(queries, self.tableName)
        table_class.addRecord(**data)
        self.destroy()
