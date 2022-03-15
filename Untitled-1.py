def checkShip(grid, ship):
    count=0
    for i in range(len(ship)):
        s = ship[i] 
        row=s[0]
        col=s[1] 
        if(grid[row][col]!=1):
            count = 1 
    if(count==1): 
        return False 
    return True