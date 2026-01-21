cube = (
        [['Y1', 'Y2', 'Y3'], ['Y4', 'Y5', 'Y6'], ['Y7', 'Y8', 'Y9']], #top
        [['B1', 'B2', 'B3'], ['B4', 'B5', 'B6'], ['B7', 'B8', 'B9']], #front
        [['R1', 'R2', 'R3'], ['R4', 'R5', 'R6'], ['R7', 'R8', 'R9']], #right
        [['G1', 'G2', 'G3'], ['G4', 'G5', 'G6'], ['G7', 'G8', 'G9']], #back
        [['O1', 'O2', 'O3'], ['O4', 'O5', 'O6'], ['O7', 'O8', 'O9']], #left
        [['W1', 'W2', 'W3'], ['W4', 'W5', 'W6'], ['W7', 'W8', 'W9']], #bottom
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

def printCube():
    print(f"Top: {cube[0]}")
    print(f"Front: {cube[1]}")
    print(f"Right: {cube[2]}")
    print(f"Back: {cube[3]}")
    print(f"Left: {cube[4]}")
    print(f"Bottom: {cube[5]}")
    
    
r()
printCube()