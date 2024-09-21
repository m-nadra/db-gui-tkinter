from tkinter import *
from tkinter import ttk
import queries

class AddWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Add record")
        self.geometry("400x300")

        ttk.Label(self, text='Name:').pack()
        self.name = ttk.Entry(self)
        self.name.pack()

        ttk.Label(self, text='Lastname:').pack()
        self.lastname = ttk.Entry(self)
        self.lastname.pack()

        ttk.Button(self, text='Add', command=self.addRecord).pack()

    def addRecord(self):
        queries.addStudent(self.name.get(), self.lastname.get())
        self.destroy()