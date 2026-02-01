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
        
        
    