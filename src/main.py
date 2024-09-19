from tkinter import *
from tkinter import ttk
import queries

class Window(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("School Manager")
        self.parent.geometry("800x600")

        self.header = Frame(self.parent)
        self.header.pack(side=TOP, fill=BOTH, padx=10, pady=10)
        self.tableFrame = Frame(self.parent)
        self.tableFrame.pack(side=TOP, fill=BOTH, padx=10)

        self.combobox = ttk.Combobox(self.header, values=['Student', 'Subject'])
        self.combobox.pack(side=RIGHT)
        self.combobox.bind("<<ComboboxSelected>>", self.displayTable)
        ttk.Label(self.header, text='Table:').pack(side=RIGHT)


    def displayTable(self, event) -> None:
        table = self.combobox.get()
        columns = []
        match table:
            case 'Student':
                table = queries.Student.get()
                columns = queries.Student.getColumnNames()
            case 'Subject':
                table = queries.Subject.get()
                columns = queries.Subject.getColumnNames()
            case _:
                return
        self.drawTable(table, columns)

    def drawTable(self, table, columns) -> None:
        try:
            self.tree.destroy()
        except AttributeError:
            pass

        self.tree = ttk.Treeview(self.tableFrame, columns=columns, show='headings')

        for column in columns:
            self.tree.heading(column, text=column)
        
        for row in table:
            self.tree.insert('', 'end', values=[column for column in row])
    
        self.tree.pack()

if __name__ == "__main__":
    root = Tk()
    app = Window(root)
    root.mainloop()
