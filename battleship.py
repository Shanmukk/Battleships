"""
Battleship Project
Name:
Roll No:
"""

from sqlite3 import Row
import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["rows"]=10
    data["col"]=10
    data["board_size"]=500
    data["cell_size"]=50
    data["numShips"]=5
    #data["temp_ship"] = test.testShip()
    data["temp_ship"] = []
    data["user_ships"] = 0
    user_board = emptyGrid(data["rows"], data["col"])
    #user_board = test.testGrid()
    com_board = emptyGrid(data["rows"], data["col"])
    com_board = addShips(com_board, data["numShips"])
    data["user_board"]=user_board
    data["com_board"]=com_board
    data["winner"] = None
    data["max"] = 50
    data["turns"]=0
    return 
    

'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data,userCanvas,data["user_board"],showShips=True) 
    drawGrid(data,compCanvas,data["com_board"],showShips=False)
    drawShip(data,userCanvas,data["temp_ship"]) 
    drawGameOver(data,userCanvas)
    #drawGameOver(data,compCanvas)
    return


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    if data["winner"] == None:
        press = getClickedCell(data,event)
        if board == "user":
            clickUserBoard(data,press[0],press[1])
        else:
            runGameTurn(data,press[0],press[1])
    pass

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    arr=[[1]*(cols) for _ in range(rows)] 
    return (arr)
    


'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    len_ship = 3
    orientation = random.randint(0,1)
    if orientation == 0:
        row_ship = [random.randint(1,8)]*len_ship
        col = random.randint(1,8 - 1)
        col_ship = list(range(col -1, col + 2))
        c = zip(row_ship, col_ship)
    else:
        col_ship = [random.randint(1,8)]*len_ship
        row = random.randint(1,8 - 1)
        row_ship = list(range(row - 1, row + 2))
        c = zip(row_ship, col_ship)
    return list(c)


    #return


'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    count=0
    for i in range(len(ship)):
        s = ship[i] 
        row=s[0]
        col=s[1] 
        if(grid[row][col]!=EMPTY_UNCLICKED):
            count = 1 
    if(count==1): 
        return False 
    return True



'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    count=0 
    while count<numShips: 
        ship = createShip() 
        if checkShip(grid,ship) == True: 
            for i in ship: 
                r = i[0] 
                c = i[1] 
                grid[r][c] = SHIP_UNCLICKED 
            count = count + 1 
    return grid


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    for i in range(data["rows"]):
        for d in range(data["col"]):
            if grid[i][d] == EMPTY_UNCLICKED:
                canvas.create_rectangle(d*data["cell_size"],i*data["cell_size"],data["cell_size"]*(d+1),data["cell_size"]*(i+1),fill="blue")
            if grid[i][d]==SHIP_UNCLICKED: 
                canvas.create_rectangle(d*data["cell_size"],i*data["cell_size"],data["cell_size"]*(d+1),data["cell_size"]*(i+1),fill="yellow") 
            elif grid[i][d] == SHIP_CLICKED:
                canvas.create_rectangle(d*data["cell_size"],i*data["cell_size"],data["cell_size"]*(d+1),data["cell_size"]*(i+1),fill="red") 
            elif grid[i][d] == EMPTY_CLICKED:
                canvas.create_rectangle(d*data["cell_size"],i*data["cell_size"],data["cell_size"]*(d+1),data["cell_size"]*(i+1),fill="white")
            if (grid[i][d] == SHIP_UNCLICKED) and showShips == False:   
                canvas.create_rectangle(d*data["cell_size"],i*data["cell_size"],data["cell_size"]*(d+1),data["cell_size"]*(i+1),fill="blue") 
    return


### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    ship.sort()
    col = ship[0][1]
    count = 0
    for i in range(len(ship)):
        if ship[i][1] == col:
            count = count+1
            if count == len(ship):
                if ship[1][0] - ship[0][0] == 1 and ship[2][0] - ship[1][0] == 1:
                    return True
                return False
        else:
            return False
    '''l = [ ] 
    col = ship[0][1] 
    count = 0 
    for i in range(len(ship)): 
        if(ship[i][1] == col): 
            count += 1 
            l.append(ship[i][0])  
            if count == (len(ship)): 
                if max(l)-min(l) == len(ship)-1: 
                    return True 
                return False 
        else:
            return False'''


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    l = [ ] 
    row = ship[0][0]
    count = 0                         
    for i in range(len(ship)): 
        if(ship[i][0] == row): 
            count += 1 
            l.append(ship[i][1])   
            if count == (len(ship)): 
                if max(l)-min(l) == 2: 
                    return True 
                return False
        else:
            return False
   


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    x,y = int(event.x / data["cell_size"]), int(event.y / data["cell_size"]) 
    return [y,x]
    


'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    for i in ship:
        canvas.create_rectangle(i[1]*data["cell_size"],i[0]*data["cell_size"],data["cell_size"]*(i[1]+1),data["cell_size"]*(i[0]+1),fill="white")
    return


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    if len(ship) == 3:
        if checkShip(grid,ship) and isVertical(ship) or isHorizontal(ship):
            return True
    return False

'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    if(shipIsValid(data["user_board"],data["temp_ship"])):
        for i in range(len(data["temp_ship"])):
            data["user_board"][data["temp_ship"][i][0]][data["temp_ship"][i][1]] = SHIP_UNCLICKED  
        data["user_ships"] += 1
    else:
        print("Ship is not valid")
    data["temp_ship"] = [] 
    return
    


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    if data["user_ships"] == 5:
        print("You can start the game")
        return
    for i in (data["temp_ship"]):
        if([row,col] == i):
            return
    data["temp_ship"].append([row,col])
    if(len(data["temp_ship"])==3):
        placeShip(data)
    return


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    if board[row][col] == SHIP_UNCLICKED:
        board[row][col] = SHIP_CLICKED
    if board[row][col] == EMPTY_UNCLICKED:
        board[row][col] = EMPTY_CLICKED
    if isGameOver(board) == True:
        data["winner"] = player
    return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    if(data["com_board"][row][col] == SHIP_CLICKED or data["com_board"][row][col] == EMPTY_CLICKED): 
        return 
    else: 
        updateBoard(data,data["com_board"] ,row,col,"user_board")
    cell = getComputerGuess(data["user_board"]) 
    updateBoard(data,data["user_board"],cell[0],cell[1],"com_board")
    data["turns"] +=1
    if data["turns"] == data["max"]:
        data["winner"] = "draw"
    return


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    row = random.randint(0,9) 
    col = random.randint(0,9) 
    while board[row][col] == SHIP_CLICKED or board[row][col] == EMPTY_CLICKED: 
        row = random.randint(0,9) 
        col = random.randint(0,9) 
    if board[row][col] == SHIP_UNCLICKED or board[row][col] == EMPTY_UNCLICKED: 
        return [row,col]



'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == SHIP_UNCLICKED:  
                return False
    return True


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    if data["winner"] == "user_board":
        canvas.create_text(250,250,text="User is the winner", fill = "black", font = "times 30", anchor = "center")
    elif data["winner"] == "com_board":
        canvas.create_text(250,250,text="Computer is the winner",fill = "black", font = "times 30" , anchor = "center")
    elif data["winner"] == "draw":
        canvas.create_text(250,250,text="Out of moves-It's Draw",fill = "black", font = "times 30" , anchor = "center")
    return


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    test.testEmptyGrid()
    test.testCreateShip()
    test.testCheckShip()
    test.testAddShips()
    test.testMakeModel()
    test.testDrawGrid()
    test.testIsVertical()
    test.testIsHorizontal()
    test.testGetClickedCell()
    test.testDrawShip()
    test.testShipIsValid()
    test.testUpdateBoard()
    test.testGetComputerGuess()
    test.testIsGameOver()

    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)
