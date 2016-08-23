class grid(object):
    """docstring for grid"""
    def __init__(self, w, h):
        super(grid, self).__init__()
        self.w = w
        self.h = h
        # Cell = [[0 for x in range(w)] for y in range(h)]
        self.Cell = [[0 for x in range(w)] for x in range(h)]
        for i in range(h):
            for j in range(w):
                self.Cell[i][j] = cell()
        print(self.Cell)

class cell(object):
    """docstring for cell"""



    def __init__(self):
        super(cell, self).__init__()

        self.color = 'def'
        self.occupied = False
        self.hit = False
