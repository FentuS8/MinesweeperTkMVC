import tkinter
import time

from Model.GameModel import MWGameModel
from View.GameView import MVGameView


class Controller(object):
    
    def __init__(self, width, height, mines_num):
        self.width = width
        self.height = height
        self.mines_num = mines_num

        self.model = MWGameModel(self.width, self.height, self.mines_num)
        self.root = tkinter.Tk()
        # self.view = MVGameView(self.root, self.width, self.height, self.mines_num)

        self.bindClicks()
        self.root.mainloop()

    # бинд нажатий открыть/флажок
    def bindClicks(self):
        for i in range(self.width):
            for j in range(self.height):
                self.view.cells_list[str(i) + ',' + str(j)] \
                    .bind(
                    '<Button-1>',
                    lambda event, index=[i, j]: self.model.open(event, index)
                )
                self.view.cells_list[str(i) + ',' + str(j)] \
                    .bind(
                    '<Button-3>',
                    lambda event, index=[i, j]: self.toFlag(event, index)
                )
        self.view.reset_btn.bind('<Button>', self.model.newGame)

    # ставит флаг
    def toFlag(self, event, index):
        i, j = index[0], index[1]
        button_index = str(i) + ',' + str(j)
        button_value = self.view.cells_list[button_index]
        if button_value["bg"] == "grey":
            button_value.configure(bg="green", text="flag")
            self.flagged_cells.append(button_index)
        elif button_value["text"] == "flag":
            button_value.configure(bg="grey", text="")
            self.flagged_cells.remove(button_index)
        self.updateMinesCounter()

    # выигрыш
    def win(self):
        self.view.deleteCells('mine')
        self.view.win()
        self.state = 'Win'

    # проигрыш
    def lose(self):
        self.view.deleteCells('mine')
        for i in range(self.width):
            for j in range(self.width):
                value = self.emptyNeighbor([i, j])
                self.openCell(value, [i, j])
        self.view.lose()
        self.state = 'Lose'
