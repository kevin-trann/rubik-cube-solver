cube = (
        [['Y1', 'Y2', 'Y3'], ['Y4', 'Y5', 'Y6'], ['Y7', 'Y8', 'Y9']], #top
        [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']], #front
        [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']], #right
        [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']], #back
        [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']], #left
        [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']], #bottom
        )

#Moves

def u():
    
    temp = cube[1][0] #temp to hold top blue row
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
    temp = cube[1][0] #temp to hold top blue row
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
    
uPrime()
print(cube) 
