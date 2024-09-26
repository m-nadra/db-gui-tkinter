from tkinter import messagebox
from abc import ABC, abstractmethod
from windows import AddWindow
import queries


class RecordOperation(ABC):
    @abstractmethod
    def execute(self):
        pass


class AddRecord(RecordOperation):
    def __init__(self, tableContent):
        self.tableContent = tableContent

    def execute(self):
        tableName = self.tableContent.tableName
        addWindow = AddWindow(tableName)
        self.tableContent.frame.wait_window(addWindow)
        self.tableContent.updateTable(tableName)


class EditRecord(RecordOperation):
    def __init__(self, tableContent):
        self.tableContent = tableContent

    def execute(self):
        pass


class DeleteRecord(RecordOperation):
    def __init__(self, tableContent):
        self.tableContent = tableContent

    def execute(self):
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
