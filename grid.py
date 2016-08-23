class grid(object):
    """docstring for grid"""
    # Cell = [][]
    def __init__(self, w, h):
        super(grid, self).__init__()
        self.w = w
        self.h = h
        # Cell = [[0 for x in range(w)] for y in range(h)]
        Cell = [[0 for x in range(w)] for x in range(h)]
        for i in range(h):
            for j in range(w):
                Cell[i][j] = cell
        print(Cell)

class cell(object):
    """docstring for cell"""

    color = 'def'
    occupied = False
    hit = False

    def __init__(self, arg):
        super(cell, self).__init__()
        self.arg = x
