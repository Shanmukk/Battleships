def isHorizantal(ship):
    ship.sort()
    row = ship[0][0]
    count = 0
    for i in range(len(ship)):
        if ship[i][0] == row:
            count = count+1
            if count == len(ship):
                if ship[1][1] - ship[0][1] == 1 and ship[2][1] - ship[1][1] == 1:
                    return True
                return False
        else:
            return False
print(isHorizantal([[1,0], [0,1], [1,2]]))
            

                
                #if max(k) - min(k) == len(ship)-1:
                  ##return False

    




