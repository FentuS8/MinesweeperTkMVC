import random
import tkinter
from datetime import datetime

from View.GameView import MVGameView


class MWGameModel(object):

    def __init__(self, width, height, mines_num, time):
        self.width = width
        self.height = height
        self.mines_num = mines_num
        self.time = time
        self.root = tkinter.Tk()
        self.view = MVGameView(self.root, width, height, mines_num, time)
        self.root.title("Minesweeper")
        self.zeros = []
        self.opened_cells = []
        self.flagged_cells = []
        self.state = None
        self.createGrid()
        self.minesCreate()
        self.bindClicks()
        self.counter_label()
        self.root.mainloop()

    # бинд нажатий открыть/флажок
    def bindClicks(self):
        for i in range(self.width):
            for j in range(self.height):
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
        # self.view.menu_btn.bind('<Button>', MWMenuController.setStatus('menu'))

    # создание поля
    def createGrid(self):
        self.grid = [[0] * self.height for i in range(self.width)]

    # создание мин
    def minesCreate(self):

        # генерация случайных координат
        def coordinates():
            row = random.randint(0, self.height - 1)
            column = random.randint(0, self.width - 1)
            return row, column

        # установка бомб
        for i in range(self.mines_num):
            row, column = coordinates()
            while self.grid[row][column] == 'bomb':
                row, column = coordinates()
            self.grid[row][column] = 'bomb'

        for i in self.grid:
            print(i)

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
            self.view.lose()
        if value == 0:
            self.emptyNeighbor(index)

    # подсчет бомб вокруг
    def minesAround(self, index):
        i, j = index[0], index[1]
        mines_num = 0
        try:
            if self.grid[i][j] == 'bomb':
                return 'bomb'
        except IndexError:
            pass

        def countMines():
            try:
                if self.grid[neighbor[0]][neighbor[1]] == 'bomb':
                    return 1
            except IndexError:
                pass
            return 0

        neighbors = [
            [i + 1, j - 1], [i + 1, j], [i + 1, j + 1], [i, j + 1],
            [i - 1, j + 1], [i - 1, j], [i - 1, j - 1], [i, j - 1]
        ]

        for neighbor in neighbors:
            if 0 <= neighbor[0] <= self.width - 1 and 0 <= neighbor[1] <= self.height - 1:
                mines_num += countMines()
        return mines_num

    # открытие клетки
    def openCell(self, value, index):
        i, j = index[0], index[1]
        closed_cells = self.height * self.width - len(self.opened_cells) - 1
        cell_coordinates = str(i) + ',' + str(j)
        if self.view.cells_list[cell_coordinates]['text'] == 'flag':
            pass
        elif value == 'bomb':
            self.view.cells_list[cell_coordinates].configure()
        else:
            if (0 <= i <= self.height - 1 and 0 <= j <= self.width and
                    [cell_coordinates] not in self.opened_cells):
                self.view.cells_list[cell_coordinates].configure(text=value, bg='white')
                self.zeros.append(cell_coordinates)
                self.opened_cells.append([cell_coordinates])

            if cell_coordinates in self.flagged_cells:
                self.flagged_cells.remove(cell_coordinates)
                self.updateMinesCounter()

            if closed_cells == self.mines_num and not self.state:
                self.view.win()

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
                if (0 <= neighbor[0] <= self.width - 1 and 0 <= neighbor[1] <= self.height - 1
                        and self.minesAround(neighbor) == 0 and neighbor not in self.zeros):
                    self.zeros.append(neighbor)
                    self.emptyNeighbor(neighbor)

    # обновляет счетчик бомб
    def updateMinesCounter(self):
        mines_left = self.mines_num - len(self.flagged_cells)
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
            if 0 <= neighbor[0] <= self.width - 1 and 0 <= neighbor[0] <= self.height - 1:
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

    # секундомер
    def counter_label(self):
        def count():
            global time_str
            if self.state is None:
                tt = datetime.fromtimestamp(self.time)
                time_str = tt.strftime("%M:%S")
                self.view.time_str.set('Ur time is: ' + str(time_str))
                self.view.stopwatch.after(1000, count)
                self.time += 1
            return time_str
        count()

    # открытие меню
    def destroyGame(self):
        from Model.AppModel import AppModel
        AppModel()
        self.root.exit()
