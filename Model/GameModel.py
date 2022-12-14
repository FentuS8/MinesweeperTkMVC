import random


class MWGameModel(object):

    def __init__(self, width, height, mines_num):
        self.width = width
        self.height = height
        self.mines_num = mines_num
        self.createGrid()
        self.minesCreate()

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