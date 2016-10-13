class Grid(object):
    
    def __init__(self, w, h):
        super(Grid, self).__init__()
        self.w = w
        self.h = h
        self.cell = [[0 for x in range(w)] for x in range(h)]
        for i in range(h):
            for j in range(w):
                self.cell[i][j] = Cell()
        print(self.cell)

class Cell(object):
    """docstring for cell"""

    def __init__(self):
        super(Cell, self).__init__()

        self.color = 'def'
        self.occupied = False
        self.hit = False
