import random
grid = [ [None for k in range(0, 9)] for i in range(0,9)]

class CellGroup(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.populate()

    def populate(self):
        self.cells = []
        for x in range(self.x, self.x+3):
            for y in range(self.y, self.y+3):
                cell = Cell(x, y, group=self)
                self.cells.append(cell)
                grid[x][y] = cell

class Cell(object):
    def __init__(self, x, y, group):
        self.group = group
        self.x, self.y = x, y
        self.value = " "

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)

def generate_grid():
    for x in range(0, 7, 3):
        for y in range(0, 7, 3):
            cell_group = CellGroup(x, y)


def check_grid(line_number):
    numbers = set([grid[line_number][x]  for x in range(0,9)])
    if len(numbers) == line_number:
        return True
    return False


def populate_grid(line_number=0):
    if line_number >= 9:
        return

    digits = range(1, 10)
    random.shuffle(digits)
    for x in range(0, 9):
        cell = grid[line_number][x]
        cell.value = digits.pop()

    if line_number > 0:
        if check_grid(line_number):
            populate_grid(line_number+1)
        else:
            populate_grid(line_number)
    
    populate_grid(line_number+1)

    print grid


generate_grid()
populate_grid()
