

class Controller(object):
    
    def __init__(self, width, height, mines_num):
        self.width = width
        self.height = height
        self.mines_num = mines_num

    # выигрыш
    def win(self):
        self.model.state = 'Win'

    # проигрыш
    def lose(self):
        for i in range(self.width):
            for j in range(self.height):
                value = self.model.emptyNeighbor([i, j])
                self.model.openCell(value, [i, j])
        self.model.state = 'Lose'
