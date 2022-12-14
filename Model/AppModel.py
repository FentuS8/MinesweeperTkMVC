import tkinter
from Controller.MenuController import MWMenuController
from Controller.Controller import Controller


class AppModel(object):
    def __init__(self, width, height, mines_num):
        self.width = width
        self.height = height
        self.mines_num = mines_num
        self.root = tkinter.Tk()
        self.status = MWMenuController.getStatus()

    def get_status(self):
        return self.status

    if get_status() == 'menu':
        MWMenuController()
    elif get_status() == 'eazy':
        Controller(10, 10, 40)
    elif get_status() == 'normal':
        Controller(10, 10, 40)
    elif get_status() == 'hard':
        Controller(10, 10, 40)



