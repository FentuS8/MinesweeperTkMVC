import tkinter

from Controller.MenuController import MWMenuController
from Model.GameModel import MWGameModel


class AppModel(object):
    def __init__(self):
        self.status = MWMenuController().getStatus()



