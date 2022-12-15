import tkinter

from Controller.Controller import Controller
from View.MenuView import MWMenuView


class MWMenuController():
    def __init__(self):
        self.root = tkinter.Tk()
        self.view = MWMenuView(self.root, self)
        self.root.title("Menu")
        self.root.geometry("200x110")
        self.root.mainloop()
        self.status = 'menu'

    def getStatus(self):
        return self.status

    def eazy(self, event):
        self.root.destroy()
        Controller(10, 10, 10)

    def normal(self, event):
        self.root.destroy()
        self.status = 'normal'

    def hard(self, event):
        self.root.destroy()
        self.status = 'hard'
