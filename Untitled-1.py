import random
def createShip():
    len_ship = 3
    orientation = random.randint(0,1)
    if orientation == 0:
        row_ship = [random.randint(1,8)]*len_ship
        col = random.randint(1,8 - len_ship)
        col_ship = list(range(col - 1, col + 2))
        c = tuple(zip(row_ship, col_ship))
    else:
        col_ship = [random.randint(1,8)]*len_ship
        row = random.randint(1,8 - len_ship)
        row_ship = list(range(row - 1, row + 2))
        c = tuple(zip(row_ship, col_ship))
    return list(co)
g = createShip()
print(g)