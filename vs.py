def isVertical(ship):
    ship.sort()
    #print(ship)
    #k = []
    col = ship[0][1]
    count = 0
    for i in range(len(ship)):
        if ship[i][1] == col:
            count = count+1
            #k.append(ship[i][0])
            #k.sort()
            if count == len(ship):
                if ship[1][0] - ship[0][0] == 1 and ship[2][0] - ship[1][0] == 1:
                #if k[1] - k[0] == 1 and k[2] - k[1] == 1:
                    return True
                return False
        else:
            return False
print(isVertical([[1,1], [2,1], [0,1]]))
            

                
                #if max(k) - min(k) == len(ship)-1:
                  ##return False

    




