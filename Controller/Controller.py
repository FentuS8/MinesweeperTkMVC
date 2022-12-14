import tkinter
import time

from Model.GameModel import MWGameModel
from View.GameView import MVGameView


class Controller(object):
    
    def __init__(self, width, height, mines_num):
        self._width = width
        self._height = height
        self._mines_num = mines_num

        self.model = MWGameModel(self._width, self._height, self._mines_num)
        self.root = tkinter.Tk()
        self.view = MVGameView(self.root, self._width, self._height, self._mines_num)

        self.zeros = []
        self.opened_cells = []
        self.flagged_cells = []
        self.state = None

        self.bindClicks()
        self.root.mainloop()

    # бинд нажатий открыть/флажок
    def bindClicks(self):
        for i in range(self._width):
            for j in range(self._height):
                self.view.cells_list[str(i) + ',' + str(j)] \
                    .bind(
                    '<Button-1>',
                    lambda event, index=[i, j]: self.open(event, index)
                )
                self.view.cells_list[str(i) + ',' + str(j)] \
                    .bind(
                    '<Button-3>',
                    lambda event, index=[i, j]: self.toFlag(event, index)
                )
        self.view.reset_btn.bind('<Button>', self.newGame)

    # обновление всего
    def newGame(self, event):
        self.zeros = []
        self.opened_cells = []
        self.flagged_cells = []
        self.state = None
        self.view.deleteCells()

        self.model = MWGameModel(self._width, self._height, self._mines_num)
        self.view = MVGameView(self.root, self._width, self._height, self._mines_num)
        self.bindClicks()

    # проверка открытия клетки
    def open(self, event, index):
        i, j = index[0], index[1]
        value = self.minesAround(index)
        if value in [x for x in range(1, 9)]:
            self.openCell(value, index)
            self.zeros.append(index)
        if (value == 'bomb' and self.state != 'Win'
                and self.view.cells_list[str(i) + ',' + str(j)]['text'] != 'flag'):
            self.state = 'Lose'
            self.lose()
        if value == 0:
            self.emptyNeighbor(index)

    # подсчет бомб вокруг
    def minesAround(self, index):
        i, j = index[0], index[1]
        mines_num = 0
        try:
            if self.model.grid[i][j] == 'bomb':
                return 'bomb'
        except IndexError:
            pass

        def countMines():
            try:
                if self.model.grid[neighbor[0]][neighbor[1]] == 'bomb':
                    return 1
            except IndexError:
                pass
            return 0

        neighbors = [
            [i + 1, j - 1], [i + 1, j], [i + 1, j + 1], [i, j + 1],
            [i - 1, j + 1], [i - 1, j], [i - 1, j - 1], [i, j - 1]
        ]

        for neighbor in neighbors:
            if 0 <= neighbor[0] <= self._width - 1 and 0 <= neighbor[1] <= self._height - 1:
                mines_num += countMines()
        return mines_num

    # открытие клетки
    def openCell(self, value, index):
        i, j = index[0], index[1]
        closed_cells = self._height * self._width - len(self.opened_cells) - 1
        cell_coordinates = str(i) + ',' + str(j)
        if self.view.cells_list[cell_coordinates]['text'] == 'flag':
            pass
        elif value == 'bomb':
            self.view.cells_list[cell_coordinates].configure(bg='black')
        else:
            if (0 <= i <= self._height - 1 and 0 <= j <= self._width and
                    [cell_coordinates] not in self.opened_cells):
                self.view.cells_list[cell_coordinates].configure(text=value, bg='white')
                self.zeros.append(cell_coordinates)
                self.opened_cells.append([cell_coordinates])

            if cell_coordinates in self.flagged_cells:
                self.flagged_cells.remove(cell_coordinates)
                self.updateMinesCounter()

            if closed_cells == self._mines_num and not self.state:
                self.win()

    # проверка для открытия пустых соседей
    def emptyNeighbor(self, index):
        i, j = index[0], index[1]
        neighbors = [
            [i + 1, j - 1], [i + 1, j], [i + 1, j + 1], [i, j + 1],
            [i - 1, j + 1], [i - 1, j], [i - 1, j - 1], [i, j - 1]
        ]
        value = self.minesAround(index)
        self.openEmpty(index)
        if value != 0:
            return None
        else:
            for neighbor in neighbors:
                if (0 <= neighbor[0] <= self._width - 1 and 0 <= neighbor[1] <= self._height - 1
                        and self.minesAround(neighbor) == 0 and neighbor not in self.zeros):
                    self.zeros.append(neighbor)
                    self.emptyNeighbor(neighbor)

    # обновляет счетчик бомб
    def updateMinesCounter(self):
        mines_left = self._mines_num - len(self.flagged_cells)
        if mines_left > 0:
            self.view.mines_left_str.set("Mines left: " + str(mines_left))

    # открытие пустых соседей
    def openEmpty(self, index):
        value = self.minesAround(index)
        self.openCell(value, index)
        i, j = index[0], index[1]
        neighbors = [
            [i + 1, j - 1], [i + 1, j], [i + 1, j + 1], [i, j + 1],
            [i - 1, j + 1], [i - 1, j], [i - 1, j - 1], [i, j - 1]
        ]
        for neighbor in neighbors:
            if 0 <= neighbor[0] <= self._width - 1 and 0 <= neighbor[0] <= self._height - 1:
                new_value = self.minesAround(neighbor)
                self.openCell(new_value, index)

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
        for i in range(self._width):
            for j in range(self._width):
                value = self.emptyNeighbor([i, j])
                self.openCell(value, [i, j])
        self.view.lose()
        self.state = 'Lose'
