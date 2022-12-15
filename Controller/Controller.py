import tkinter
import time

from Model.GameModel import MWGameModel
from View.GameView import MVGameView


class Controller(object):
    
    def __init__(self, width, height, mines_num):
        self.width = width
        self.height = height
        self.mines_num = mines_num
        # self.model = MWGameModel(self.width, self.height, self.mines_num)

    # выигрыш
    def win(self):
        self.view.deleteCells('bomb')
        self.view.win()
        self.state = 'Win'

    # проигрыш
    def lose(self):
        self.view.deleteCells('bomb')
        for i in range(self.width):
            for j in range(self.height):
                value = self.emptyNeighbor([i, j])
                self.openCell(value, [i, j])
        self.view.lose()
        self.state = 'Lose'
