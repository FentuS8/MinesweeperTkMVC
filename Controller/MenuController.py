import tkinter

from View.MenuView import MWMenuView


class MWMenuController:
    def __init__(self):
        self.root = tkinter.Tk()
        self.view = MWMenuView(self.root, self)
        self.root.title("Menu")
        self.root.geometry("200x110")
        self.status = None
        self.root.mainloop()

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status
        self.root.destroy()

    def easy(self, event):
        self.setStatus('easy')

    def medium(self, event):
        self.setStatus('medium')

    def hard(self, event):
        self.setStatus('hard')

    def menu(self, event):
        self.setStatus('menu')
