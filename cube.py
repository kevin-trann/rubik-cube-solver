import random

cube = (
        [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']], #top
        [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']], #front
        [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']], #right
        [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']], #back
        [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']], #left
        [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']], #bottom
        )

scrambleSequence = []

#sequence of moves for entire solution
solutionSequence = []

#sequence of moves for each step
crossSequence = []
f2lSequence = []
ollSequence = []
pllSequence = []

moveCount = 0

#Moves

def u(addToSolutionSequence=True):
    
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
    
    if addToSolutionSequence:
        solutionSequence.append('U')



def uPrime(addToSolutionSequence=True):
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
    
    if addToSolutionSequence:
        solutionSequence.append('U\'')

def u2(addToSolutionSequence=True):
    u(addToSolutionSequence=False)
    u(addToSolutionSequence=False)
    if addToSolutionSequence:
        solutionSequence.append('U2')
    
def r(addToSolutionSequence=True):
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
    
    if addToSolutionSequence:
        solutionSequence.append('R')
    
def rPrime(addToSolutionSequence=True):
    r(addToSolutionSequence=False)
    r(addToSolutionSequence=False)
    r(addToSolutionSequence=False)
    if addToSolutionSequence:
        solutionSequence.append('R\'')
    
def r2(addToSolutionSequence=True):
    r(addToSolutionSequence=False)
    r(addToSolutionSequence=False)
    if addToSolutionSequence:
        solutionSequence.append('R2')
    
def wideR(addToSolutionSequence=True):
    m(addToSolutionSequence=False)
    r(addToSolutionSequence=False)
    if addToSolutionSequence:
        solutionSequence.append('r')

def wideRPrime(addToSolutionSequence=True):
    mPrime(addToSolutionSequence=False)
    rPrime(addToSolutionSequence=False)
    if addToSolutionSequence:
        solutionSequence.append('r\'')

def m(addToSolutionSequence=True):
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
    if addToSolutionSequence:
        solutionSequence.append('M')

def m2(addToSolutionSequence=True):
    m(addToSolutionSequence=False)
    m(addToSolutionSequence=False)
    if addToSolutionSequence:
        solutionSequence.append('M2')

def mPrime(addToSolutionSequence=True):
    m(addToSolutionSequence=False)
    m(addToSolutionSequence=False)
    m(addToSolutionSequence=False)
    if addToSolutionSequence:
        solutionSequence.append('M\'')
    
def l(addToSolutionSequence=True):
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
    
    if addToSolutionSequence:
        solutionSequence.append('L')
    
def lPrime(addToSolutionSequence=True):
    l(addToSolutionSequence=False)
    l(addToSolutionSequence=False)
    l(addToSolutionSequence=False)
    
    if addToSolutionSequence:
        solutionSequence.append('L\'')
    
def l2(addToSolutionSequence=True):
    l(addToSolutionSequence=False)
    l(addToSolutionSequence=False)
    if addToSolutionSequence:
        solutionSequence.append('L2')
    
def b(addToSolutionSequence=True):
    
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
    if addToSolutionSequence:
        solutionSequence.append('B')
    
def bPrime(addToSolutionSequence=True):
    b(addToSolutionSequence=False)
    b(addToSolutionSequence=False)
    b(addToSolutionSequence=False)
    if addToSolutionSequence:
        solutionSequence.append('B\'')
    
def b2(addToSolutionSequence=True):
    b(addToSolutionSequence=False)
    b(addToSolutionSequence=False)
    if addToSolutionSequence:
        solutionSequence.append('B2')

def d(addToSolutionSequence=True):
    
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
    if addToSolutionSequence:
        solutionSequence.append('D')

def dPrime(addToSolutionSequence=True):
    d(addToSolutionSequence=False)
    d(addToSolutionSequence=False)
    d(addToSolutionSequence=False)
    if addToSolutionSequence:
        solutionSequence.append('D\'')
    
def d2(addToSolutionSequence=True):
    d(addToSolutionSequence=False)
    d(addToSolutionSequence=False)
    if addToSolutionSequence:
        solutionSequence.append('D2')
    
def f(addToSolutionSequence=True):
    
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
    
    if addToSolutionSequence:
        solutionSequence.append('F')
    
    
def fPrime(addToSolutionSequence=True):
    f(addToSolutionSequence=False)
    f(addToSolutionSequence=False)
    f(addToSolutionSequence=False)
    if addToSolutionSequence:
        solutionSequence.append('F\'')

def f2(addToSolutionSequence=True):
    f(addToSolutionSequence=False)
    f(addToSolutionSequence=False)
    if addToSolutionSequence:
        solutionSequence.append('F2')
    
def wideF(addToSolutionSequence=True):
    f(addToSolutionSequence=False)
    
    #temp holds middle yellow row
    temp = cube[0][1].copy()
    
    #change middle yellow row to middle orange pieces
    cube[0][1][0] = cube[4][2][1]
    cube[0][1][1] = cube[4][1][1]
    cube[0][1][2] = cube[4][0][1]
    
    #change middle orange pieces to middle white row
    cube[4][0][1] = cube[5][1][0]
    cube[4][1][1] = cube[5][1][1]
    cube[4][2][1] = cube[5][1][2]
    
    #change middle white row to middle red pieces
    cube[5][1][0] = cube[2][2][1]
    cube[5][1][1] = cube[2][1][1]
    cube[5][1][2] = cube[2][0][1]
    
    #change middle red pieces to middle yellow row
    cube[2][0][1] = temp[0]
    cube[2][1][1] = temp[1]
    cube[2][2][1] = temp[2]
    
    if addToSolutionSequence:
        solutionSequence.append('f')

def wideFPrime(addToSolutionSequence=True):
    
    wideF(addToSolutionSequence=False)
    wideF(addToSolutionSequence=False)
    wideF(addToSolutionSequence=False)
    
    if addToSolutionSequence:
        solutionSequence.append('f\'')
    
def randomizeCube():
    #reset solutionSequence and other sequences
    scrambleSequence.clear()
    solutionSequence.clear()
    
    crossSequence.clear()
    f2lSequence.clear()
    ollSequence.clear()
    pllSequence.clear()
    
    #array containing all possible moes on cube
    moveSet = [r, rPrime, r2, l, lPrime, l2, f, fPrime, f2, b, bPrime, b2, u, uPrime, u2, d, dPrime, d2]
    
    #hashMap to make sure redudant moves are added to scramble sequence
    conflictedMovesMap = {'r' : ['rPrime', 'r', 'r2'], 'rPrime' : ['r', 'rPrime', 'r2'], 'r2' : ['r2', 'r', 'rPrime'], 'l' : ['lPrime', 'l', 'l2'], 'lPrime' : ['l', 'lPrime', 'l2'], 'l2' : ['l2', 'l', 'lPrime'], 'm' : ['mPrime', 'm', 'm2'], 'mPrime' : ['m', 'm2', 'mPrime'], 'm2' : ['m2', 'm', 'mPrime'], 
    'f' : ['fPrime', 'f', 'f2'], 'fPrime' : ['fPrime', 'f', 'f2'], 'f2' : ['fPrime', 'f', 'f2'], 'b' : ['b', 'bPrime', 'b2'], 'bPrime' : ['b', 'bPrime', 'b2'], 'b2' : ['b', 'bPrime', 'b2'], 'u' : ['u', 'uPrime', 'u2'], 'uPrime': ['u', 'uPrime', 'u2'], 'u2' : ['u', 'uPrime', 'u2'], 'd' : ['d', 'dPrime', 'd2'], 'dPrime' : ['d', 'dPrime', 'd2'], 'd2' : ['d', 'dPrime', 'd2']}
    
    #hashMap for move to append to randomized moveset
    randomMoves = {'r' : 'R', 'rPrime' : 'R\'', 'r2' : 'R2', 'l' : 'L', 'lPrime' : 'L\'', 'l2' : 'L2', 'm' : 'M', 'mPrime' : 'M\'', 'm2' : 'M2',
    'f' : 'F', 'fPrime' : 'F\'', 'f2' : 'F2', 'b' : 'B', 'bPrime' : 'B\'', 'b2' : 'B2', 'u' : 'U', 'uPrime': 'U\'', 'u2' : 'U2', 'd' : 'D', 'dPrime' : 'D\'', 'd2' : 'D2'}
    
    
    
    count = 0
    
    while count < 21:
        
        move = random.choice(moveSet)
        
        if count > 0 and scrambleSequence[count - 1] in conflictedMovesMap.get(move.__name__):
            continue
        
        scrambleSequence.append(randomMoves[move.__name__])
        move(addToSolutionSequence=False)
        
        count += 1
    
    addToSolutionSequence = True
    
    
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

def getCubeState():
    return{
        "Top" : cube[0],
        "Front" : cube[1],
        "Right" : cube[2],
        "Back" : cube[3],
        "Left" : cube[4],
        "Bottom" : cube[5],
    }
    
def getSolutionSequence():
    return solutionSequence()
