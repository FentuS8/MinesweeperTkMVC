import tkinter
from tkinter import messagebox


class MVGameView(tkinter.Frame):

    def __init__(self, master, width, height, mines_num):
        tkinter.Frame.__init__(self, master)
        self.cells_list = {}
        self.master = master
        self.width = width
        self.height = height
        self.mines_num = mines_num
        self.grid()
        self.topBar()
        self.addCells()

    # верхняя панель
    def topBar(self):
        self.reset_btn = tkinter.Button(self.master, width=5, text='Reset')
        self.reset_btn.grid(row=0, column=int(self.width/4), columnspan=2)

        self.menu_btn = tkinter.Button(self.master, width=5, text='Menu')
        self.menu_btn.grid(row=0, column=int(self.width/4)*2, columnspan=2)
        # self.menu_btn.bind("<Button>")

        self.mines_left_str = tkinter.StringVar()
        self.mines_left_str.set('Mines left: ' + str(self.mines_num))
        self.mines_left = tkinter.Label(textvariable=self.mines_left_str)
        self.mines_left.grid(row=0, column=int(self.width/4)*3, columnspan=3)

        self.time_str = tkinter.StringVar()
        self.time_str.set('Ur time is: 0')
        self.time = tkinter.Label(textvariable=self.time_str)
        self.time.grid(row=0, column=int(self.width/4)*4, columnspan=2)

    # добавление ячеек
    def addCells(self):
        for i in range(self.width):
            for j in range(self.height):
                self.cells_list[str(i) + "," + str(j)] = \
                    tkinter.Button(self.master, width=5, height=2, background="grey")
                self.cells_list[str(i) + ',' + str(j)].grid(row=i + 1, column=j + 1)

    # удаление ячеек
    def deleteCells(self, condition=None):
        if condition:
            self.mines_left.grid_remove()
        else:
            # self.panel.lose_text.grid_remove()
            # self.panel.win_text.grid_remove()
            pass

    # победа вывод
    def win(self):
        win = messagebox.showinfo(
            "WIN",
            "Grats! U won!"
        )
        return win

    # поражение вывод
    def lose(self):
        lose = messagebox.showinfo(
            "LOSE",
            "Grats! U're loser!"
        )
        return lose
