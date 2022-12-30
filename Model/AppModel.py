
from Controller.MenuController import MWMenuController
from Model.GameModel import MWGameModel


class AppModel:
    def __init__(self):
        self.menu = MWMenuController()
        self.status = self.menu.getStatus()
        # print(self.status)
        self.setWindow()

    def setWindow(self):
        if self.status == 'easy':
            MWGameModel(10, 10, 3, 0)
        elif self.status == 'medium':
            MWGameModel(12, 12, 50, 0)
        elif self.status == 'hard':
            MWGameModel(15, 15, 70, 0)
        elif self.status == 'menu':
            AppModel()
