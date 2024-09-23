from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from add import AddWindow
import queries

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("School Manager")
        self.geometry("800x600")

        self.header = Header(self)
        self.table = Table(self)
        self.options = Options(self)


class Header(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(anchor='ne', padx=50, pady=10)
        ttk.Label(self, text='Table:').pack(side=LEFT)
        self.combobox = ttk.Combobox(self, values=queries.getTablesNames())
        self.combobox.pack(side=RIGHT, fill=BOTH)
        self.combobox.bind("<<ComboboxSelected>>", lambda _: parent.table.drawTable(self.combobox.get()))


class Table(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side=TOP, fill=BOTH, expand=True, padx=50, pady=10)
        self.tree = ttk.Treeview(self, show='headings')
        self.tree.pack(expand=True, fill=BOTH)

    def drawTable(self, tableName) -> None:
        try:
            self.tree.destroy()
        except AttributeError:
            pass
        
        tableClass = getattr(queries, tableName, None)
        
        if tableClass is None:
            return

        records = tableClass.get()
        columns = tableClass.getColumnNames()

        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        for column in columns:
            self.tree.heading(column, text=column)
        
        for row in records:
            self.tree.insert('', 'end', values=[column for column in row])
    
        self.tree.pack(expand=True, fill=BOTH)


class Options(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text='Options')
        self.parent = parent
        self.pack(side=BOTTOM, padx=50, pady=50, ipady=10)

        ttk.Button(self, text='Add', command=self.add).pack(side=LEFT, padx=10)
        ttk.Button(self, text='Edit', command=self.edit).pack(side=LEFT, padx=10)
        ttk.Button(self, text='Delete', command=self.delete).pack(side=LEFT, padx=10)
   
    def add(self) -> None:
        AddWindow(self.parent.header.combobox.get())

    def edit(self) -> None:
        pass

    def delete(self) -> None:
        try:
            recordId = self.parent.table.tree.item(self.parent.table.tree.selection())['values'][0]
        except IndexError:
            messagebox.showerror("Error", "No record selected")
            return
        result = messagebox.askquestion("Confirm deletion", "Do you want to remove record?") 
        if result == 'no':
            return
        tableName = self.parent.header.combobox.get()
        tableClass = getattr(queries, tableName, None)
        tableClass.deleteRecord(recordId)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
