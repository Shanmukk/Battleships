"""
Battleship Project
Name:
Roll No:
"""

from pickle import LIST
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
    data["no.of rows"]=10
    data["no.of cols"]=10
    data["board size"]=500
    data["no.of ships"]=5
    #data["temp_ship"]=test.testShip()
    data["temp_ship"]=[]
    data["cell size"]=data["board size"]/data["no.of rows"]
    data["no.of_userships"]=0
    data["computer"]=emptyGrid(data["no.of rows"],data["no.of cols"])
    data["user"]=emptyGrid(data["no.of rows"],data["no.of cols"])
    #data["user"]=test.testGrid()
    data["computer"]=addShips(data["computer"],data["no.of ships"])
    #data["user"]=user
#   data["computer"]=computer
    return 


'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data,userCanvas,data["user"],showShips=True)
    drawGrid(data,compCanvas,data["computer"],showShips=True)
    #drawShip(data,userCanvas,data["temp_ship"])
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
    pass

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
   # g = [[1]*(cols)]*(rows)
    #return g 
    #a=10 
    #b=20 
    list=[[1]*(cols) for row in range(rows)]
    return (list)
    #done 
    

'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
#def createShip():
    #lst=[rows][cols]
    #row=3
    #col=7
    #randomnumber= 1
#for i in range(row)
#    lst[3][6]="4"
#    lst[3][7]="5"
#    lst[3][8]="6"
#    return
def createShip(): 
    len_ship = 3 
    orientation = random.randint(0,1) 
    if orientation == 0: 
        row_ship = [random.randint(1,8 - 1)]*len_ship 
        centre = random.randint(1,8 - len_ship)  
        lst=[centre-1,centre,centre+1]
        combined= tuple(zip(row_ship, lst)) 
    else: 
        col_ship = [random.randint(1,8 - 1)]*len_ship 
        centre = random.randint(1,8 - len_ship)  
        lst=[centre-1,centre,centre+1]
        combined = tuple(zip(lst, col_ship))
    return list(combined)

'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    count = 0 
    i=0 
    while i<len(ship): 
        l = ship[i] 
        l1=l[0] 
        l2=l[1] 
        if(grid[l1][l2]!=EMPTY_UNCLICKED): 
            count = 1 
        i = i+1 
    if(count==0): 
        return True
    return  False
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
            for coordinates in ship: 
                l1 = coordinates[0] 
                l2 = coordinates[1] 
                grid[l1][l2] = SHIP_UNCLICKED 
            count = count + 1 
    return grid


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips): 
    for i in range(data["no.of rows"]):
        for j in range(data["no.of cols"]):
                    if (grid[i][j]==SHIP_UNCLICKED):
                        canvas.create_rectangle(j*data["cell size"],i*data["cell size"],data["cell size"]*(j+1),data["cell size"]*(i+1),fill="yellow")
                    else:
                        canvas.create_rectangle(j*data["cell size"],i*data["cell size"],data["cell size"]*(j+1),data["cell size"]*(i+1),fill="blue")

#canvas.create_rectangle(0*(i+1),0*(j+1),50*(i+1),50*(j+1))
"""def draw(canvas): 
        pass 
    def makeCanvas(w,h): 
        root = tk.Tk() 
        canvas = tk.Canvas(root, width=w, height=h) 
        canvas.configure(bd=0, highlightthickness=0) 
        for i in range(10):
            canvas.create_line(data["board size"]*i,0,50*i,500,fill)
            canvas.create_line(0,50*i,500,50*i)
        canvas.pack() 
        draw(canvas) 
        root.mainloop() 
    makeCanvas(500,500)
    return
    testGrid(Canvas)"""


### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
#lst=[ [2, 1], [0, 1], [1, 1] ]
    lst1=[ ]
    column=ship[0][1] 
    count=0
    for i in range (len(ship)):
        if (ship[i][1] == column):
            count+=1
            lst1.append(ship[i][0])
        else:
            return False
#    print(lst1)
    if (count==len(ship)):
        if((max(lst1)-min(lst1))==(len(ship))-1):
            return True
        else: 
            return False
#    return



'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
#[ [1, 0], [1, 1], [1, 2] ]
    lst1=[ ]
    row=ship[0][0] #1
    count=0
    for i in range (len(ship)):
        if (ship[i][0] == row):
            count+=1
            lst1.append(ship[i][1])
        else:
            return False
#    print(lst1)
    if (count==len(ship)):
        if((max(lst1)-min(lst1))==(len(ship))-1):
            return True
        else: 
            return False
    return
    

'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
#    lst = []
    x,y = int(event.x / data["cell size"]), int(event.y / data["cell size"])
#    lst.append(y)
#    lst.append(x)
        #x = int(event.x / data["cell_size"])
        #lst.append(x)
    return [y,x]
    return 



'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    for i in range(len(ship)):
        x,y=ship[i][0],ship[i][1]
        canvas.create_rectangle(y*data["cell size"],x* data["cell size"],(y+1)* data["cell size"],(x+1)* data["cell size"],fill="white")
    return



'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    if(len(ship)==3):
        if(checkShip(grid,ship) and isVertical(ship) or isHorizontal(ship)):
            return True
    return False



'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    if(shipIsValid(data["user"],data["temp_ship"])):
        for i in range(len(data["temp_ship"])):
            data["user"][data["temp_ship"][i][0]][data["temp_ship"][i][1]] = SHIP_UNCLICKED
            #data["user_board"]=data
        data["no.of_userships"]+=1  
    else:
        print("Ship is not valid")
    data["temp_ship"]=[]
    return
#data["boarduser"][data["temporaryShip"][i][0]][data["temporaryShip"][i][1]]=SHIP_UNCLICKED

'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    if data["no.of_userships"]==5:
        print("You can start the game")
        return
    for i in (data["temp_ship"]):
        if([row,col] == i):
            return
        #else:
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
    return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    return


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    return


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    return


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
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
    

    
    

    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)
