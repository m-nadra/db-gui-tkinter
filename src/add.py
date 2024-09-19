from tkinter import *
from tkinter import ttk

class AddWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Add record")
        self.geometry("400x300")