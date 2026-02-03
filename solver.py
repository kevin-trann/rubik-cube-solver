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
     upperBottomRightCorner, lowerUpperLeftCorner, lowerUpperRightCorner,
     lowerBottomLeftCorner, lowerBottomRightCorner, upperTopEdge, 
     upperLeftEdge, upperRightEdge, upperBottomEdge, backLeftEdge,
     backRightEdge, frontLeftEdge, frontRightEdge, lowerTopEdge,
     lowerLeftEdge, lowerRightEdge, lowerBottomEdge) = changeCubeState()
    
    #checks if blue red pair is valid
    while lowerBottomRightCorner != ['W', 'B', 'R'] or frontRightEdge != ['B', 'R']:
        
        (upperTopLeftCorner, upperTopRightCorner, upperBottomLeftCorner, 
        upperBottomRightCorner, lowerUpperLeftCorner, lowerUpperRightCorner,
        lowerBottomLeftCorner, lowerBottomRightCorner, upperTopEdge, 
        upperLeftEdge, upperRightEdge, upperBottomEdge, backLeftEdge,
        backRightEdge, frontLeftEdge, frontRightEdge, lowerTopEdge,
        lowerLeftEdge, lowerRightEdge, lowerBottomEdge) = changeCubeState()
        
        #checks if white blue red piece is in proper corner(base case)
        if 'W' in upperBottomRightCorner and 'B' in upperBottomRightCorner and 'R' in upperBottomRightCorner:
            
            #white is facing blue side
            if upperBottomRightCorner[1] == 'W':
                
                #blue, red in upper right edge
                if upperRightEdge == ['B', 'R']:
                    u()
                    r()
                    uPrime()
                    rPrime()
                    continue
                
                if upperRightEdge == ['R', 'B']:
                    uPrime()
                    r()
                    u2()
                    rPrime()
                    u()
                    fPrime()
                    uPrime()
                    f()
                    continue
                
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
                    continue
                    
                if upperTopEdge == ['R', 'B']:
                    uPrime()
                    r()
                    uPrime()
                    rPrime()
                    u()
                    fPrime()
                    uPrime()
                    f()
                    continue
                
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
                    continue
                
                if upperLeftEdge == ['R', 'B']:
                    fPrime()
                    uPrime()
                    f()
                    continue
                
                #blue, red in upper bottom edge
                
                if upperBottomEdge == ['B', 'R']:
                    fPrime()
                    u()
                    f()
                    u2()
                    r()
                    u()
                    rPrime()
                    continue
                
                if upperBottomEdge == ['R', 'B']:
                    u()
                    fPrime()
                    u()
                    f()
                    uPrime()
                    fPrime()
                    uPrime()
                    f()
                    continue
                    
                

                
            
        
                
            
        
            
                
    
        print(upperTopLeftCorner)
        print(upperTopRightCorner)
        print(upperBottomLeftCorner)
        print(upperBottomRightCorner)  
        print("")  
        print(lowerUpperLeftCorner)  
        print(lowerUpperRightCorner)  
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