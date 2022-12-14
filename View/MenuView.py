import tkinter


class MWMenuView():
    def __init__(self, master, controller):
        self.controller = controller
        self.frame = tkinter.Frame(master)
        self.frame.pack()
        self.viewPanel = ViewPanel(master, controller)


class ViewPanel():
    def __init__(self, root, controller):
        self.controller = controller

        self.menu = tkinter.Frame(root)
        self.menu.pack()

        self.btn = tkinter.Button(self.menu, text="EAZY")
        self.btn.pack()
        self.btn.bind("<Button>", controller.eazy)

        self.btn = tkinter.Button(self.menu, text="NORMAL")
        self.btn.pack()
        self.btn.bind("<Button>", controller.normal)

        self.btn2 = tkinter.Button(self.menu, text="HARD")
        self.btn2.pack()
        self.btn2.bind("<Button>", controller.hard)

        self.info = tkinter.Label(text='ALLERT!\nU may lose from the first step!')
        self.info.pack()
