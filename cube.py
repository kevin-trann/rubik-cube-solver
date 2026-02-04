import random

cube = (
        [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']], #top
        [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']], #front
        [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']], #right
        [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']], #back
        [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']], #left
        [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']], #bottom
        )

#Moves

def u():
    
    temp = cube[1][0].copy() #temp to hold top blue row
    cube[1][0] = cube[2][0] #change top blue row to top red row
    cube[2][0] = cube[3][0] #change top red row to top green row
    cube[3][0] = cube[4][0] #change top green row to top orange row
    cube[4][0] = temp #change top orange row to top blue row
    
    #changing top pieces
    newTopRow = [ cube[0][2][0], cube[0][1][0], cube[0][0][0]]
    newMiddleRow = [ cube[0][2][1], cube[0][1][1], cube[0][0][1]]
    newBottomRow = [ cube[0][2][2], cube[0][1][2], cube[0][0][2]]
    
    cube[0][0] = newTopRow 
    cube[0][1] = newMiddleRow
    cube[0][2] = newBottomRow
   
def uPrime():
    temp = cube[1][0].copy() #temp to hold top blue row
    cube[1][0] = cube[4][0] #change top blue row to top orange row
    cube[4][0] = cube[3][0] #change top orange row to top green row
    cube[3][0] = cube[2][0] #change top green row to top red row
    cube[2][0] = temp #change top red row to top blue row
    
    #changing top pieces
    #3, 6, 9, : 2, 5, 8 : 1, 4, 7
    newTopRow = [ cube[0][0][2], cube[0][1][2], cube[0][2][2]]
    newMiddleRow = [ cube[0][0][1], cube[0][1][1], cube[0][2][1]]
    newBottomRow = [ cube[0][0][0], cube[0][1][0], cube[0][2][0]]
    
    cube[0][0] = newTopRow 
    cube[0][1] = newMiddleRow
    cube[0][2] = newBottomRow

def u2():
    u()
    u()
    
def r():
    temp = [ cube[1][0][2], cube[1][1][2], cube[1][2][2]]  #hold right blue column

    #change blue right column to white right column
    cube[1][0][2] = cube[5][0][2]
    cube[1][1][2] = cube[5][1][2]
    cube[1][2][2] = cube[5][2][2]
    
    #change white right column to green left column
    cube[5][0][2] = cube[3][2][0]
    cube[5][1][2] = cube[3][1][0]
    cube[5][2][2] = cube[3][0][0]
    
    #change green left column to yellow right column
    cube[3][0][0] = cube[0][2][2]
    cube[3][1][0] = cube[0][1][2]
    cube[3][2][0] = cube[0][0][2]
    
    #change yellow right column to blue right column    
    for i in range(3):
         cube[0][i][2] = temp[i]
         
    #changing right pieces
    # 7, 4, 1 : 8, 5, 2 : 9, 6, 3
    newTopRow = [ cube[2][2][0], cube[2][1][0], cube[2][0][0]]
    newMiddleRow = [ cube[2][2][1], cube[2][1][1], cube[2][0][1]]
    newBottomRow = [ cube[2][2][2], cube[2][1][2], cube[2][0][2]]
    
    cube[2][0] = newTopRow 
    cube[2][1] = newMiddleRow
    cube[2][2] = newBottomRow
    
def rPrime():
    r()
    r()
    r()
    
def r2():
    r()
    r()

def m():
    temp = [cube[1][0][1], cube[1][1][1], cube[1][2][1]] #temp holds blue middle column
    
    #change middle blue column to middle white column
    cube[1][0][1] = cube[5][0][1]
    cube[1][1][1] = cube[5][1][1]
    cube[1][2][1] = cube[5][2][1]
    
    #change middle white column to middle green column
    # 8, 5, 2
    cube[5][0][1] = cube[3][2][1]
    cube[5][1][1] = cube[3][1][1]
    cube[5][2][1] = cube[3][0][1]
    
    #change middle green column to middle
    # 2, 5, 7
    cube[3][2][1] = cube[0][0][1]
    cube[3][1][1] = cube[0][1][1]
    cube[3][0][1] = cube[0][2][1]
    
    #change middle yellow column to middle blue column
    for i in range(3):
         cube[0][i][1] = temp[i]

def m2():
    m()
    m()

def mPrime():
    m()
    m()
    m()
    
def l():
    #temp to hold left blue column
    temp = [cube[1][0][0], cube[1][1][0], cube[1][2][0]]
    
    #change left blue column to left yellow column
    cube[1][0][0] = cube[0][0][0]
    cube[1][1][0] = cube[0][1][0]
    cube[1][2][0] = cube[0][2][0]
    
    #change left yellow column to right green column
    #9, 6, 3
    cube[0][0][0] = cube[3][2][2]
    cube[0][1][0] = cube[3][1][2]
    cube[0][2][0] = cube[3][0][2]
    
    #change right green column to left white column
    #7, 4, 1
    cube[3][0][2] = cube[5][2][0] 
    cube[3][1][2] = cube[5][1][0]
    cube[3][2][2] = cube[5][0][0]
    
    #change left white column to left blue column
    for i in range(3):
        cube[5][i][0] = temp[i]
        
    #changing left pieces
    # 7, 4, 1 : 8, 5, 2 : 9, 6, 3
    newTopRow = [ cube[4][2][0], cube[4][1][0], cube[4][0][0]]
    newMiddleRow = [ cube[4][2][1], cube[4][1][1], cube[4][0][1]]
    newBottomRow = [ cube[4][2][2], cube[4][1][2], cube[4][0][2]]
    
    cube[4][0] = newTopRow 
    cube[4][1] = newMiddleRow
    cube[4][2] = newBottomRow
    
def lPrime():
    l()
    l()
    l()
    
def l2():
    l()
    l()
    
def b():
    
    #temp to hold top yellow row
    temp = cube[0][0].copy()
    
    #change top yellow row to right red column
    cube[0][0][0] = cube[2][0][2]
    cube[0][0][1] = cube[2][1][2]
    cube[0][0][2] = cube[2][2][2]
    
    #change right red column to bottom white row
    cube[2][0][2] = cube[5][2][2]
    cube[2][1][2] = cube[5][2][1]
    cube[2][2][2] = cube[5][2][0]
    
    #change bottom white row to left orange column
    cube[5][2][0] = cube[4][0][0]
    cube[5][2][1] = cube[4][1][0]
    cube[5][2][2] = cube[4][2][0]
    
    #change left orange column to top yellow row
    for i in range(3):
        j = 2 - i
        cube[4][i][0] = temp[j]
        
    #changing back pieces
    # 7, 4, 1 : 8, 5, 2 : 9, 6, 3
    newTopRow = [ cube[3][2][0], cube[3][1][0], cube[3][0][0]]
    newMiddleRow = [ cube[3][2][1], cube[3][1][1], cube[3][0][1]]
    newBottomRow = [ cube[3][2][2], cube[3][1][2], cube[3][0][2]]
    
    cube[3][0] = newTopRow 
    cube[3][1] = newMiddleRow
    cube[3][2] = newBottomRow
    
def bPrime():
    b()
    b()
    b()
    
def b2():
    b()
    b()

def d():
    
    #temp to hold bottom orange row
    temp = cube[4][2].copy()
    
    #bottom orange row to bottom green row
    cube[4][2] = cube[3][2]
    
    #bottom green row to bottom red row
    cube[3][2] = cube[2][2]
    
    #bottom red row to bottom blue row
    cube[2][2] = cube[1][2]
    
    #change bottom blue row to bottom orange row
    cube[1][2] = temp
    
    #changing bottom pieces
    # 7, 4, 1 : 8, 5, 2 : 9, 6, 3
    newTopRow = [ cube[5][2][0], cube[5][1][0], cube[5][0][0]]
    newMiddleRow = [ cube[5][2][1], cube[5][1][1], cube[5][0][1]]
    newBottomRow = [ cube[5][2][2], cube[5][1][2], cube[5][0][2]]
    
    cube[5][0] = newTopRow 
    cube[5][1] = newMiddleRow
    cube[5][2] = newBottomRow

def dPrime():
    d()
    d()
    d()
    
def d2():
    d()
    d()
    
def f():
    
    # numbers switch but colours stay the same so check this if anything bugs out
    
    #temp to hold bottom yellow row
    temp = cube[0][2].copy()
    
    #change bottom yellow row to right orange column
    cube[0][2][0] = cube[4][2][2]
    cube[0][2][1] = cube[4][1][2]
    cube[0][2][2] = cube[4][0][2]
    
    #change right orange column to top white row
    cube[4][0][2] = cube[5][0][0]
    cube[4][1][2] = cube[5][0][1]
    cube[4][2][2] = cube[5][0][2]
    
    #change top white row to left red column
    cube[5][0][0] = cube[2][2][0]
    cube[5][0][1] = cube[2][1][0]
    cube[5][0][2] = cube[2][0][0]
    
    #change left red column to bottom yellow row
    for i in range(3):
        cube[2][i][0] = temp[i]
        
    #changing front pieces
    # 7, 4, 1 : 8, 5, 2 : 9, 6, 3
    newTopRow = [ cube[1][2][0], cube[1][1][0], cube[1][0][0]]
    newMiddleRow = [ cube[1][2][1], cube[1][1][1], cube[1][0][1]]
    newBottomRow = [ cube[1][2][2], cube[1][1][2], cube[1][0][2]]
    
    cube[1][0] = newTopRow 
    cube[1][1] = newMiddleRow
    cube[1][2] = newBottomRow
    
    
def fPrime():
    f()
    f()
    f()

def f2():
    f()
    f()
    
def randomizeCube():
    #array containing all possible moes on cube
    moveSet = [r, rPrime, r2, l, lPrime, l2, f, fPrime, f2, b, bPrime, b2, u, uPrime, u2, d, dPrime, d2]
    
    #hashMap to make sure redudant moves are added to scramble sequence
    conflictedMovesMap = {'r' : ['rPrime', 'r', 'r2'], 'rPrime' : ['r', 'rPrime', 'r2'], 'r2' : ['r2', 'r', 'rPrime'], 'l' : ['lPrime', 'l', 'l2'], 'lPrime' : ['l', 'lPrime', 'l2'], 'l2' : ['l2', 'l', 'lPrime'], 'm' : ['mPrime', 'm', 'm2'], 'mPrime' : ['m', 'm2', 'mPrime'], 'm2' : ['m2', 'm', 'mPrime'], 
    'f' : ['fPrime', 'f', 'f2'], 'fPrime' : ['fPrime', 'f', 'f2'], 'f2' : ['fPrime', 'f', 'f2'], 'b' : ['b', 'bPrime', 'b2'], 'bPrime' : ['b', 'bPrime', 'b2'], 'b2' : ['b', 'bPrime', 'b2'], 'u' : ['u', 'uPrime', 'u2'], 'uPrime': ['u', 'uPrime', 'u2'], 'u2' : ['u', 'uPrime', 'u2'], 'd' : ['d', 'dPrime', 'd2'], 'dPrime' : ['d', 'dPrime', 'd2'], 'd2' : ['d', 'dPrime', 'd2']}
    
    #array to hold the instructions to get to scrambled state
    scrambleSequence = []
    
    count = 0
    
    while count < 11:
        
        move = random.choice(moveSet)
        
        if count > 0 and scrambleSequence[count - 1] in conflictedMovesMap.get(move.__name__):
            continue
        
        scrambleSequence.append(move.__name__)
        move()
        
        count += 1
        

    print(F"Scramble Sequence: {scrambleSequence}")  
    
#function to keep track of piece states
def changeCubeState():
    upperTopLeftCorner = [cube[0][0][0], cube[3][0][2], cube[4][0][0]]
    upperTopRightCorner = [cube[0][0][2], cube[2][0][2], cube[3][0][0]]
    upperBottomLeftCorner = [cube[0][2][0], cube[4][0][2], cube[1][0][0]]
    upperBottomRightCorner = [cube[0][2][2], cube[1][0][2], cube[2][0][0]]
    
    lowerTopLeftCorner = [cube[5][2][0], cube[3][2][2], cube[4][2][0]]
    lowerTopRightCorner = [cube[5][2][2], cube[2][2][2], cube[3][2][0]]
    lowerBottomLeftCorner = [cube[5][0][0], cube[4][2][2], cube[1][2][0]]
    lowerBottomRightCorner = [cube[5][0][2], cube[1][2][2], cube[2][2][0]]
    
    upperTopEdge = [cube[0][0][1], cube[3][0][1]]
    upperLeftEdge = [cube[0][1][0], cube[4][0][1]]
    upperRightEdge = [cube[0][1][2], cube[2][0][1]]
    upperBottomEdge = [cube[0][2][1], cube[1][0][1]]
    
    backLeftEdge = [cube[3][1][2], cube[4][1][0]]
    backRightEdge = [cube[2][1][2], cube[3][1][0]]
    frontLeftEdge = [cube[4][1][2], cube[1][1][0]]
    frontRightEdge = [cube[1][1][2], cube[2][1][0]]
    
    lowerTopEdge = [cube[5][2][1], cube[3][2][1]]
    lowerLeftEdge = [cube[5][1][0], cube[4][2][1]]
    lowerRightEdge = [cube[5][1][2], cube[2][2][1]]
    lowerBottomEdge = [cube[5][0][1], cube[1][2][1]]
    
    return (upperTopLeftCorner, upperTopRightCorner, upperBottomLeftCorner, 
            upperBottomRightCorner, lowerTopLeftCorner, lowerTopRightCorner,
            lowerBottomLeftCorner, lowerBottomRightCorner, upperTopEdge, 
            upperLeftEdge, upperRightEdge, upperBottomEdge, backLeftEdge,
            backRightEdge, frontLeftEdge, frontRightEdge, lowerTopEdge,
            lowerLeftEdge, lowerRightEdge, lowerBottomEdge)

    #function to print cube state to test/debug
def printCube():
    print("")
    print(f"Top: {cube[0]}")
    print(f"Front: {cube[1]}")
    print(f"Right: {cube[2]}")
    print(f"Back: {cube[3]}")
    print(f"Left: {cube[4]}")
    print(f"Bottom: {cube[5]}")
    print("")
