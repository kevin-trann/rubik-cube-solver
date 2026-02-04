from cube import *
#functions to solve cube
#cross solver
def crossSolver():
    while (cube[5][0][1] != 'W' or cube[1][2][1] != 'B') or (cube[5][1][0] != 'W' or cube[4][2][1] != 'O') or (cube[5][1][2] != 'W' or cube[2][2][1] != 'R') or (cube[5][2][1] != 'W' or cube[3][2][1] != 'G'):
        
        #check top edge pieces
        #checks top back edge 
        if cube[0][0][1] == 'W':
            if cube[3][0][1] == 'G':
                b2()
                
            if cube[3][0][1] == 'R':
                u()
                r2()
            
            if cube[3][0][1] == 'B':
                u2()
                f2()
                
            if cube[3][0][1] == 'O':
                uPrime()
                l2()
            continue
        
        #checks top left edge
        if cube[0][1][0] == 'W':
            if cube[4][0][1] == 'G':
                u()
                b2()
                
            if cube[4][0][1] == 'R':
                u2()
                r2()
            
            if cube[4][0][1] == 'B':
                uPrime()
                f2()
                
            if cube[4][0][1] == 'O':
                l2()
            continue

        #checks top right edge
        if cube[0][1][2] == 'W':
            if cube[2][0][1] == 'G':
                uPrime()
                b2()
                
            if cube[2][0][1] == 'R':
                r2()
            
            if cube[2][0][1] == 'B':
                u()
                f2()
                
            if cube[2][0][1] == 'O':
                u2()
                l2()
            continue

        #checks top bottom edge
        if cube[0][2][1] == 'W':
            if cube[1][0][1] == 'G':
                u2()
                b2()
                
            if cube[1][0][1] == 'R':
                uPrime()
                r2()
            
            if cube[1][0][1] == 'B':
                f2()
                
            if cube[1][0][1] == 'O':
                u()
                l2()
        
            continue

        #checks front side for white edges
        #checks top edge
        if cube[1][0][1] == "W":
            f()
            r()
            uPrime()
            rPrime()
            fPrime()
            continue
        
        #checks left edge
        if cube[1][1][0] == "W":
            lPrime()
            uPrime()
            l()
            continue
        
        #checks right edge 
        if cube[1][1][2] == "W":
            r()
            u()
            rPrime()
            continue
        
        #checks bottom edge
        if cube[1][2][1] == "W":
            fPrime()
            r()
            u()
            rPrime()
            continue
        
        
        #checks right side for white edges
        #checks top edge
        if cube[2][0][1] == "W":
            
            r()
            b()
            uPrime()
            bPrime()
            rPrime()
            continue
        
        #checks left edge
        if cube[2][1][0] == "W":
            
            fPrime()
            uPrime()
            f()
            continue
        
        #checks right edge 
        if cube[2][1][2] == "W":
            b()
            u()
            bPrime()
            continue
        
        #checks bottom edge
        if cube[2][2][1] == "W":    
            rPrime()
            b()
            u()
            bPrime()
            continue
        
        
        #checks left side for white edges
        #checks top edge
        if cube[4][0][1] == "W":
            l()
            f()
            uPrime()
            fPrime()
            lPrime()
            continue
        
        #checks left edge
        if cube[4][1][0] == "W":
            bPrime()
            uPrime()
            b()
            continue
        
        #checks right edge 
        if cube[4][1][2] == "W":            
            f()
            u()
            fPrime()
            continue
        
        #checks bottom edge
        if cube[4][2][1] == "W":
            lPrime()
            f()
            u()
            fPrime()
            continue
        
        #checks back side for white edges
        #checks top edge
        if cube[3][0][1] == "W": 
            b()
            l()
            uPrime()
            lPrime()
            bPrime()
            continue
        
        #checks left edge
        if cube[3][1][0] == "W":
            rPrime()
            uPrime()
            r()
            continue
        
        #checks right edge 
        if cube[3][1][2] == "W":
            l()
            u()
            lPrime()
            continue
        
        #checks bottom edge
        if cube[3][2][1] == "W":
            bPrime()
            l()
            u()
            lPrime()
            continue
        
        #checks if all botttom white edges are oriented correctly
        if cube[1][2][1] != "B":
            f2()
            continue
        
        if cube[2][2][1] != "R":
            r2()
            continue
        
        if cube[4][2][1] != "O":
            l2()
            continue
        
        if cube[3][2][1] != "G":
            b2()
            continue

#function to solve f2l step
def f2lSolver():
    
    #updates cube states
    (upperTopLeftCorner, upperTopRightCorner, upperBottomLeftCorner, 
     upperBottomRightCorner, lowerTopLeftCorner, lowerTopRightCorner,
     lowerBottomLeftCorner, lowerBottomRightCorner, upperTopEdge, 
     upperLeftEdge, upperRightEdge, upperBottomEdge, backLeftEdge,
     backRightEdge, frontLeftEdge, frontRightEdge, lowerTopEdge,
     lowerLeftEdge, lowerRightEdge, lowerBottomEdge) = changeCubeState()
    
    while 'B' not in upperBottomRightCorner or 'W' not in upperBottomRightCorner or 'R' not in upperBottomRightCorner:
        
        (upperTopLeftCorner, upperTopRightCorner, upperBottomLeftCorner, 
        upperBottomRightCorner, lowerTopLeftCorner, lowerTopRightCorner,
        lowerBottomLeftCorner, lowerBottomRightCorner, upperTopEdge, 
        upperLeftEdge, upperRightEdge, upperBottomEdge, backLeftEdge,
        backRightEdge, frontLeftEdge, frontRightEdge, lowerTopEdge,
        lowerLeftEdge, lowerRightEdge, lowerBottomEdge) = changeCubeState()
            
        #moves the corner piece to base case position
        if 'W' in upperTopLeftCorner and 'B' in upperTopLeftCorner and 'R' in upperTopLeftCorner:
            u2()
            continue
        
        if 'W' in upperTopRightCorner and 'B' in upperTopRightCorner and 'R' in upperTopRightCorner:
            u()
            continue
        
        if 'W' in upperBottomLeftCorner and 'B' in upperBottomLeftCorner and 'R' in upperBottomLeftCorner:
            uPrime()
            continue
        
        if 'W' in lowerTopLeftCorner and 'B' in lowerTopLeftCorner and 'R' in lowerTopLeftCorner:
            l()
            u2()
            lPrime()
            continue
        
        if 'W' in lowerTopRightCorner and 'B' in lowerTopRightCorner and 'R' in lowerTopRightCorner:
            rPrime()
            u2()
            r()
            uPrime()
            continue
        
        if 'W' in lowerBottomLeftCorner and 'B' in lowerBottomLeftCorner and 'R' in lowerBottomLeftCorner:
            lPrime()
            uPrime()
            l()
            continue
        
        if 'W' in lowerBottomRightCorner and 'B' in lowerBottomRightCorner and 'R' in lowerBottomRightCorner:
            r()
            u()
            rPrime()
            uPrime()
            continue
        
#moves blue red edge piece to top layer (base case)
    
    if 'R' in backLeftEdge and 'B' in backLeftEdge:
        l()
        uPrime()
        lPrime()
        u()
    
    if 'R' in backRightEdge and 'B' in backRightEdge:
        u()
        rPrime()
        u()
        r()
        u2()
    
    if 'R' in frontLeftEdge and 'B' in frontLeftEdge:
        lPrime()
        uPrime()
        l()
        u()
    
    if 'R' in frontRightEdge and 'B' in frontRightEdge:
        u()
        r()
        u()
        rPrime()
        u2()
    
    (upperTopLeftCorner, upperTopRightCorner, upperBottomLeftCorner, 
    upperBottomRightCorner, lowerTopLeftCorner, lowerTopRightCorner,
    lowerBottomLeftCorner, lowerBottomRightCorner, upperTopEdge, 
    upperLeftEdge, upperRightEdge, upperBottomEdge, backLeftEdge,
    backRightEdge, frontLeftEdge, frontRightEdge, lowerTopEdge,
    lowerLeftEdge, lowerRightEdge, lowerBottomEdge) = changeCubeState()
    
    #white is facing front side
    if upperBottomRightCorner[1] == 'W':
        print("YAY")
        #blue, red in upper right edge
        if upperRightEdge == ['B', 'R']:
            u()
            r()
            uPrime()
            rPrime()
            
        
        if upperRightEdge == ['R', 'B']:
            uPrime()
            r()
            u2()
            rPrime()
            u()
            fPrime()
            uPrime()
            f()
        
        #blue, red in upper top edge
        if upperTopEdge == ['B', 'R']:
            uPrime()
            r()
            u()
            rPrime()
            u2()
            r()
            uPrime()
            rPrime()
            
        if upperTopEdge == ['R', 'B']:
            uPrime()
            r()
            uPrime()
            rPrime()
            u()
            fPrime()
            uPrime()
            f()

        #blue, red in upper left edge
        
        if upperLeftEdge == ['B', 'R']:
            uPrime()
            r()
            u2()
            rPrime()
            u2()
            r()
            uPrime()
            rPrime()
            
        
        if upperLeftEdge == ['R', 'B']:
            fPrime()
            uPrime()
            f()
            
        
        #blue, red in upper bottom edge
        
        if upperBottomEdge == ['B', 'R']:
            fPrime()
            u()
            f()
            u2()
            r()
            u()
            rPrime()
            
        
        if upperBottomEdge == ['R', 'B']:
            u()
            fPrime()
            u()
            f()
            uPrime()
            fPrime()
            uPrime()
            f()
            

    #white facing right side
    if upperBottomRightCorner[2] == 'W':
        print("YAY2")
        #blue, red in upper right edge
        if upperRightEdge == ['B', 'R']:
            uPrime()
            r()
            uPrime()
            rPrime()
            u()
            r()
            u()
            rPrime()
        
        if upperRightEdge == ['R', 'B']:
            r()
            uPrime()
            rPrime()
            u2()
            fPrime()
            uPrime()
            f()
        
        #blue, red in upper top edge
        if upperTopEdge == ['B', 'R']:
            r()
            u()
            rPrime()
            
        if upperTopEdge == ['R', 'B']:
            u()
            fPrime()
            u2()
            f()
            u2()
            fPrime()
            u()
            f()
        
        #blue, red in upper left edge
        
        if upperLeftEdge == ['B', 'R']:
            uPrime()
            r()
            u()
            rPrime()
            u()
            r()
            u()
            rPrime()
        
        if upperLeftEdge == ['R', 'B']:
            u()
            fPrime()
            uPrime()
            f()
            u2()
            fPrime()
            u()
            f()
        
        #blue, red in upper bottom edge
        
        if upperBottomEdge == ['B', 'R']:
            u()
            fPrime()
            u2()
            f()
            uPrime()
            r()
            u()
            rPrime()
        
        if upperBottomEdge == ['R', 'B']:
            uPrime()
            fPrime()
            u()
            f()
        
    #white facing up
    if upperBottomRightCorner[0] == 'W':
        print("YAY3")
        #blue, red in upper right edge
        if upperRightEdge == ['B', 'R']:
            r()
            u2()
            rPrime()
            uPrime()
            r()
            u()
            rPrime()
        
        if upperRightEdge == ['R', 'B']:
            f()
            u()
            r()
            uPrime()
            rPrime()
            fPrime()
            r()
            uPrime()
            rPrime()
        
        #blue, red in upper top edge
        if upperTopEdge == ['B', 'R']:
            u()
            r()
            u2()
            rPrime()
            u()
            r()
            uPrime()
            rPrime()
            
        if upperTopEdge == ['R', 'B']:
            u2()
            fPrime()
            uPrime()
            f()
            uPrime()
            fPrime()
            u()
            f()
 
        #blue, red in upper left edge
        
        if upperLeftEdge == ['B', 'R']:
            u2()
            r()
            u()
            rPrime()
            u()
            r()
            uPrime()
            rPrime()
           
        if upperLeftEdge == ['R', 'B']:
            uPrime()
            fPrime()
            u2()
            f()
            uPrime()
            fPrime()
            u()
            f()
           
        #blue, red in upper bottom edge
        
        if upperBottomEdge == ['B', 'R']:
            u()
            r()
            uPrime()
            rPrime()
            uPrime()
            r()
            uPrime()
            rPrime()
            u()
            r()
            uPrime()
            rPrime()
           
        if upperBottomEdge == ['R', 'B']:
            u()
            fPrime()
            u2()
            f()
            u()
            fPrime()
            uPrime()
            f()
            uPrime()
            fPrime()
            u()
            f()
                
    """
        print(upperTopLeftCorner)
        print(upperTopRightCorner)
        print(upperBottomLeftCorner)
        print(upperBottomRightCorner)  
        print("")  
        print(lowerTopLeftCorner)  
        print(lowerTopRightCorner)  
        print(lowerBottomLeftCorner)
        print(lowerBottomRightCorner)
        print("")  
        print(upperTopEdge)
        print(upperLeftEdge)
        print(upperRightEdge)
        print(upperBottomEdge)
        print("")  
        print(backLeftEdge)
        print(backRightEdge)
        print(frontLeftEdge)
        print(frontRightEdge)
        print("")  
        print(lowerTopEdge)
        print(lowerLeftEdge)
        print(lowerRightEdge)
        print(lowerBottomEdge)
        print("")  
        """