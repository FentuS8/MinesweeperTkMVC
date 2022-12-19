import tkinter

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

    def setStatus(self, status):
        self.status = status

    def easy(self, event):
        self.root.destroy()
        self.setStatus('easy')

    def medium(self, event):
        self.root.destroy()
        self.setStatus('medium')

    def hard(self, event):
        self.root.destroy()
        self.setStatus('hard')
