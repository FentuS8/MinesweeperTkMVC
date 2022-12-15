import tkinter

from View.MenuView import MWMenuView
from Model.GameModel import MWGameModel


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

    def easy(self, event):
        self.root.destroy()
        MWGameModel(11, 11, 40)

    def medium(self, event):
        self.root.destroy()
        MWGameModel(14, 14, 70)

    def hard(self, event):
        self.root.destroy()
        MWGameModel(18, 18, 140)
