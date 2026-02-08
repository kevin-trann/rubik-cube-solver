from cube import *

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

    (upperTopLeftCorner, upperTopRightCorner, upperBottomLeftCorner, 
    upperBottomRightCorner, lowerTopLeftCorner, lowerTopRightCorner,
    lowerBottomLeftCorner, lowerBottomRightCorner, upperTopEdge, 
    upperLeftEdge, upperRightEdge, upperBottomEdge, backLeftEdge,
    backRightEdge, frontLeftEdge, frontRightEdge, lowerTopEdge,
    lowerLeftEdge, lowerRightEdge, lowerBottomEdge) = changeCubeState()
    
    #move yellow orange blue corner to base case
    
    if 'W' in lowerTopLeftCorner and 'O' in lowerTopLeftCorner and 'B' in lowerTopLeftCorner:
        l()
        u2()
        lPrime()
        u()
    
    if 'W' in lowerTopRightCorner and 'O' in lowerTopRightCorner and 'B' in lowerTopRightCorner:
        rPrime()
        u2()
        r()
        
    if 'W' in lowerBottomLeftCorner and 'O' in lowerBottomLeftCorner and 'B' in lowerBottomLeftCorner:
        lPrime()
        uPrime()
        l()
        u()
        
    if 'W' in upperBottomRightCorner and 'O' in upperBottomRightCorner and 'B' in upperBottomRightCorner:
        u()
    
    if 'W' in upperTopRightCorner and 'O' in upperTopRightCorner and 'B' in upperTopRightCorner:
        u2()
        
    if 'W' in upperTopLeftCorner and 'O' in upperTopLeftCorner and 'B' in upperTopLeftCorner:
        uPrime()
    
    (upperTopLeftCorner, upperTopRightCorner, upperBottomLeftCorner, 
    upperBottomRightCorner, lowerTopLeftCorner, lowerTopRightCorner,
    lowerBottomLeftCorner, lowerBottomRightCorner, upperTopEdge, 
    upperLeftEdge, upperRightEdge, upperBottomEdge, backLeftEdge,
    backRightEdge, frontLeftEdge, frontRightEdge, lowerTopEdge,
    lowerLeftEdge, lowerRightEdge, lowerBottomEdge) = changeCubeState()
    
    #move orange blue edge piece to top layer
    
    if 'O' in frontLeftEdge and 'B' in frontLeftEdge:
        u()
        f()
        u()
        fPrime()
        u2()
        
    if 'O' in backLeftEdge and 'B' in backLeftEdge:
        l()
        u()
        lPrime()
        
    if 'O' in backRightEdge and 'B' in backRightEdge:
        rPrime()
        u()
        r()
        uPrime()
    
    (upperTopLeftCorner, upperTopRightCorner, upperBottomLeftCorner, 
    upperBottomRightCorner, lowerTopLeftCorner, lowerTopRightCorner,
    lowerBottomLeftCorner, lowerBottomRightCorner, upperTopEdge, 
    upperLeftEdge, upperRightEdge, upperBottomEdge, backLeftEdge,
    backRightEdge, frontLeftEdge, frontRightEdge, lowerTopEdge,
    lowerLeftEdge, lowerRightEdge, lowerBottomEdge) = changeCubeState()
    
    #white facing up
    if upperBottomLeftCorner[0] == 'W':
        
        if upperRightEdge == ['B', 'O']:
            u2()
            lPrime()
            uPrime()
            l()
            uPrime()
            lPrime()
            u()
            l()
        
        if upperRightEdge == ['O', 'B']:
            u()
            f()
            u2()
            fPrime()
            u()
            f()
            uPrime()
            fPrime()
            
        if upperTopEdge == ['B', 'O']:
            uPrime()
            lPrime()
            u2()
            l()
            uPrime()
            lPrime()
            u()
            l()
            
        if upperTopEdge == ['O', 'B']:
            u2()
            f()
            u()
            fPrime()
            u()
            f()
            uPrime()
            fPrime()
            
        if upperLeftEdge == ['B', 'O']:
            lPrime()
            u2()
            l()
            u()
            lPrime()
            uPrime()
            l()
        
        if upperLeftEdge == ['O', 'B']:
            u()
            lPrime()
            u()
            l()
            u()
            f()
            u()
            fPrime()
            u()
            f()
            uPrime()
            fPrime()
            
        if upperBottomEdge == ['B', 'O']:
            l()
            u()
            f()
            uPrime()
            fPrime()
            lPrime()
            f()
            uPrime()
            fPrime()

        if upperBottomEdge == ['O', 'B']:
            f()
            u2()
            fPrime()
            uPrime()
            f()
            u()
            fPrime()
    
    #white face front
    if upperBottomLeftCorner[2] == 'W':
        
        if upperRightEdge == ['B', 'O']:
            u()
            lPrime()
            u2()
            l()
            u2()
            lPrime()
            u()
            l()
            
        if upperRightEdge == ['O', 'B']:
            f()
            u()
            fPrime()
        if upperTopEdge == ['B', 'O']:
            u()
            lPrime()
            uPrime()
            l()
            u2()
            lPrime()
            u()
            l()
            
        if upperTopEdge == ['O', 'B']:
            u()
            lPrime()
            u() 
            l()
            uPrime()
            f()
            u()
            fPrime()
            
        if upperLeftEdge == ['B', 'O']:
            uPrime()
            lPrime()
            u()
            l()
        if upperLeftEdge == ['O', 'B']:
            u()
            lPrime()
            u2()
            l()
            uPrime()
            f()
            u()
            fPrime()
        if upperBottomEdge == ['B', 'O']:
            f()
            uPrime()
            fPrime()
            u2()
            lPrime()
            uPrime()
            l()
        if upperBottomEdge == ['O', 'B']:
            l()
            uPrime()
            lPrime()
            f()
            u()
            fPrime()
            
    #white face left
    if upperBottomLeftCorner[1] == 'W':
        
        if upperRightEdge == ['B', 'O']:
            l()
            uPrime()
            l2()
            uPrime()
            l()
        if upperRightEdge == ['O', 'B']:
            l()
            u()
            lPrime()
            u()
            f()
            uPrime()
            fPrime()
        if upperTopEdge == ['B', 'O']:
            lPrime()
            uPrime()
            l()
            
        if upperTopEdge == ['O', 'B']:
            uPrime()
            f()
            u2()
            fPrime()
            u2()
            f()
            uPrime()
            fPrime()
        if upperLeftEdge == ['B', 'O']:
            u()
            lPrime()
            u()
            l()
            uPrime()
            lPrime()
            uPrime()
            l()
        if upperLeftEdge == ['O', 'B']:
            lPrime()
            u()
            l()
            u2()
            f()
            u()
            fPrime()
        if upperBottomEdge == ['B', 'O']:
            uPrime()
            f()
            u2()
            fPrime()
            u()
            lPrime()
            uPrime()
            l()

        if upperBottomEdge == ['O', 'B']:
            u()
            f()
            uPrime()
            fPrime()
    
    (upperTopLeftCorner, upperTopRightCorner, upperBottomLeftCorner, 
    upperBottomRightCorner, lowerTopLeftCorner, lowerTopRightCorner,
    lowerBottomLeftCorner, lowerBottomRightCorner, upperTopEdge, 
    upperLeftEdge, upperRightEdge, upperBottomEdge, backLeftEdge,
    backRightEdge, frontLeftEdge, frontRightEdge, lowerTopEdge,
    lowerLeftEdge, lowerRightEdge, lowerBottomEdge) = changeCubeState()

    #move orange green corner to top layer(base case)

    if 'W' in lowerTopLeftCorner and 'G' in lowerTopLeftCorner and 'O' in lowerTopLeftCorner:
        l()
        u()
        lPrime()
        uPrime()

    if 'W' in lowerTopRightCorner and 'G' in lowerTopRightCorner and 'O' in lowerTopRightCorner:
        rPrime()
        uPrime()
        r()

    if 'W' in upperTopRightCorner and 'G' in upperTopRightCorner and 'O' in upperTopRightCorner:
        uPrime()

    if 'W' in upperBottomRightCorner and 'G' in upperBottomRightCorner and 'O' in upperBottomRightCorner:
        u2()
    
    if 'W' in upperBottomLeftCorner and 'G' in upperBottomLeftCorner and 'O' in upperBottomLeftCorner:
        u()

    (upperTopLeftCorner, upperTopRightCorner, upperBottomLeftCorner, 
    upperBottomRightCorner, lowerTopLeftCorner, lowerTopRightCorner,
    lowerBottomLeftCorner, lowerBottomRightCorner, upperTopEdge, 
    upperLeftEdge, upperRightEdge, upperBottomEdge, backLeftEdge,
    backRightEdge, frontLeftEdge, frontRightEdge, lowerTopEdge,
    lowerLeftEdge, lowerRightEdge, lowerBottomEdge) = changeCubeState()

    #move orange green edge to top layer
    if 'G' in backLeftEdge and 'O' in backLeftEdge:
        l()
        uPrime()
        lPrime()
        u2()

    if 'G' in backRightEdge and 'O' in backRightEdge:
        rPrime()
        uPrime()
        r()
        u()

    (upperTopLeftCorner, upperTopRightCorner, upperBottomLeftCorner, 
    upperBottomRightCorner, lowerTopLeftCorner, lowerTopRightCorner,
    lowerBottomLeftCorner, lowerBottomRightCorner, upperTopEdge, 
    upperLeftEdge, upperRightEdge, upperBottomEdge, backLeftEdge,
    backRightEdge, frontLeftEdge, frontRightEdge, lowerTopEdge,
    lowerLeftEdge, lowerRightEdge, lowerBottomEdge) = changeCubeState()

    #white facing up
    if upperTopLeftCorner[0] == 'W':
        
        if upperBottomEdge == ['O', 'G']:
            u2()
            bPrime()
            uPrime()
            b()
            uPrime()
            bPrime()
            u()
            b()
        
        if upperBottomEdge == ['G', 'O']:
            u()
            l()
            u2()
            lPrime()
            u()
            l()
            uPrime()
            lPrime()

        if upperRightEdge == ['O', 'G']:
            uPrime()
            bPrime()
            u2()
            b()
            uPrime()
            bPrime()
            u()
            b()

        if upperRightEdge == ['G', 'O']:
            u2()
            l()
            u()
            lPrime()
            u()
            l()
            uPrime()
            lPrime()

        if upperTopEdge == ['O', 'G']:
            bPrime()
            u2()
            b()
            u()
            bPrime()
            uPrime()
            b()

        if upperTopEdge == ['G', 'O']:
            bPrime()
            u2()
            b()
            u()
            b()
            u2()
            bPrime()
            u()
            l()
            uPrime()
            lPrime()
    
        if upperLeftEdge == ['O', 'G']:
            b()
            u2()
            bPrime()
            uPrime()
            bPrime()
            u2()
            b()
            uPrime()
            bPrime()
            u()
            b()

        if upperLeftEdge == ['G', 'O']:
            l()
            u2()
            lPrime()
            uPrime()
            l()
            u()
            lPrime()

    #white facing left
    if upperTopLeftCorner[2] == 'W':

        if upperBottomEdge == ['O', 'G']:
            u()
            bPrime()
            u2()
            b()
            u2()
            bPrime()
            u()
            b()

        if upperBottomEdge == ['G', 'O']:
            l()
            u()
            lPrime()

        if upperRightEdge == ['O', 'G']:
            u()
            bPrime()
            uPrime()
            b()
            u2()
            bPrime()
            u()
            b()

        if upperRightEdge == ['G', 'O']:
            u()
            bPrime()
            u()
            b()
            uPrime()
            l()
            u()
            lPrime()

        if upperTopEdge == ['O', 'G']:
            uPrime()
            bPrime()
            u()
            b()

        if upperTopEdge == ['G', 'O']:
            u()
            bPrime()
            u2()
            b()
            uPrime()
            l()
            u()
            lPrime()

        if upperLeftEdge == ['O', 'G']:
            l()
            uPrime()
            lPrime()
            u2()
            bPrime()
            uPrime()
            b()

        if upperLeftEdge == ['G', 'O']:
            uPrime()
            l() 
            uPrime()
            lPrime()
            u()
            l()
            u()
            lPrime()

    #white facing back
    if upperTopLeftCorner[1] == 'W':

        if upperBottomEdge == ['O', 'G']:
            uPrime()
            l()
            uPrime()
            lPrime()
            u()
            bPrime()
            uPrime()
            b() 

        if upperBottomEdge == ['G', 'O']:
            uPrime()
            l()
            u()
            lPrime()
            u2()
            l()
            uPrime()
            lPrime()

        if upperRightEdge == ['O', 'G']:
            bPrime()
            uPrime()
            b()
        if upperRightEdge == ['G', 'O']:
            uPrime()
            l()
            u2()
            lPrime()
            u2()
            l()
            uPrime()
            lPrime()

        if upperTopEdge == ['O', 'G']:
            u()
            bPrime()
            u()
            b()
            uPrime()
            bPrime()
            uPrime()
            b()
        if upperTopEdge == ['G', 'O']:
            bPrime()
            u()
            b()
            u2()
            l()
            u()
            lPrime()
        if upperLeftEdge == ['O', 'G']:
            uPrime()
            l()
            u2()
            lPrime()
            u()
            bPrime()
            uPrime()
            b()
        if upperLeftEdge == ['G', 'O']:
            u()
            l()
            uPrime()
            lPrime()

    (upperTopLeftCorner, upperTopRightCorner, upperBottomLeftCorner, 
    upperBottomRightCorner, lowerTopLeftCorner, lowerTopRightCorner,
    lowerBottomLeftCorner, lowerBottomRightCorner, upperTopEdge, 
    upperLeftEdge, upperRightEdge, upperBottomEdge, backLeftEdge,
    backRightEdge, frontLeftEdge, frontRightEdge, lowerTopEdge,
    lowerLeftEdge, lowerRightEdge, lowerBottomEdge) = changeCubeState()

    #move red green corner white to top layer(base case)
    if lowerBottomRightCorner != ['W', 'R', 'G'] or backRightEdge != ['R', 'G']:
        if 'W' in lowerTopRightCorner and 'G' in lowerTopRightCorner and 'R' in lowerTopRightCorner:
            rPrime()
            uPrime()
            r()
            u()
        if 'W' in upperTopLeftCorner and 'G' in upperTopLeftCorner and 'R' in upperTopLeftCorner:
            u()
        if 'W' in upperBottomRightCorner and 'G' in upperBottomRightCorner and 'R' in upperBottomRightCorner:
            uPrime()
        if 'W' in upperBottomLeftCorner and 'G' in upperBottomLeftCorner and 'R' in upperBottomLeftCorner:
            u2()

        (upperTopLeftCorner, upperTopRightCorner, upperBottomLeftCorner, 
        upperBottomRightCorner, lowerTopLeftCorner, lowerTopRightCorner,
        lowerBottomLeftCorner, lowerBottomRightCorner, upperTopEdge, 
        upperLeftEdge, upperRightEdge, upperBottomEdge, backLeftEdge,
        backRightEdge, frontLeftEdge, frontRightEdge, lowerTopEdge,
        lowerLeftEdge, lowerRightEdge, lowerBottomEdge) = changeCubeState()

        #move red green edge to top layer

        if 'G' in backRightEdge and 'R' in backRightEdge:
            u2()
            rPrime()
            u()
            r()
            u()
        (upperTopLeftCorner, upperTopRightCorner, upperBottomLeftCorner, 
        upperBottomRightCorner, lowerTopLeftCorner, lowerTopRightCorner,
        lowerBottomLeftCorner, lowerBottomRightCorner, upperTopEdge, 
        upperLeftEdge, upperRightEdge, upperBottomEdge, backLeftEdge,
        backRightEdge, frontLeftEdge, frontRightEdge, lowerTopEdge,
        lowerLeftEdge, lowerRightEdge, lowerBottomEdge) = changeCubeState()

        #white facing up
        if upperTopRightCorner[0] == 'W':
            
            if upperBottomEdge == ['R', 'G']:
                u2()
                b()
                u()
                bPrime()
                u()
                b()
                uPrime()
                bPrime()

            if upperBottomEdge == ['G', 'R']:
                uPrime()
                rPrime()
                u2()
                r()
                uPrime()
                rPrime()
                u()
                r()

            if upperRightEdge == ['R', 'G']:
                u()
                rPrime()
                u2()
                r()
                b()
                u2()
                bPrime()
                u()
                b()
                uPrime()
                bPrime()

            if upperRightEdge == ['G', 'R']:
                rPrime()
                u2()
                r()
                u()
                rPrime()
                uPrime()
                r()

            if upperTopEdge == ['R', 'G']:
                b()
                u2()
                bPrime()
                uPrime()
                b()
                u()
                bPrime()

            if upperTopEdge == ['G', 'R']:
                b()
                u2()
                bPrime()
                rPrime()
                u2()
                r()
                u2()
                rPrime()
                u()
                r()

            if upperLeftEdge == ['R', 'G']:
                u()
                b()
                u2()
                bPrime()
                u()
                b()
                uPrime()
                bPrime()

            if upperLeftEdge == ['G', 'R']:
                u2()
                rPrime()
                uPrime()
                r()
                uPrime()
                rPrime()
                u()
                r()
        #white facing right
        if upperTopRightCorner[1] == 'W':
            
            if upperBottomEdge == ['R', 'G']:
                uPrime()
                b()
                u2()
                bPrime()
                u2()
                b()
                uPrime()
                bPrime()
                
            if upperBottomEdge == ['G', 'R']:
                rPrime()
                uPrime()
                r()

            if upperRightEdge == ['R', 'G']:
                rPrime()
                u()
                r()
                u2()
                b()
                u()
                bPrime()

            if upperRightEdge == ['G', 'R']:
                u()
                rPrime()
                u()
                r()
                uPrime()
                rPrime()
                uPrime()
                r()

            if upperTopEdge == ['R', 'G']:
                u()
                b()
                uPrime()
                bPrime()

            if upperTopEdge == ['G', 'R']:
                uPrime()
                b()
                u2()
                bPrime()
                u()
                rPrime()
                uPrime()
                r()

            if upperLeftEdge == ['R', 'G']:
                uPrime()
                b()
                u()
                bPrime()
                u2()
                b()
                uPrime()
                bPrime()

            if upperLeftEdge == ['G', 'R']:
                u()
                rPrime()
                uPrime()
                r()
                uPrime()
                rPrime()
                uPrime()
                r()

        #white facing back
        if upperTopRightCorner[2] == 'W':
            
            if upperBottomEdge == ['R', 'G']:
                u()
                rPrime()
                u()
                r()
                uPrime()
                b()
                u()
                bPrime()

            if upperBottomEdge == ['G', 'R']:
                u()
                rPrime()
                uPrime()
                r()
                u2()
                rPrime()
                u()
                r()

            if upperRightEdge == ['R', 'G']:
                u()
                rPrime()
                u2()
                r()
                uPrime()
                b()
                u()
                bPrime()

            if upperRightEdge == ['G', 'R']:
                uPrime()
                rPrime()
                u()
                r()

            if upperTopEdge == ['R', 'G']:
                uPrime()
                b()
                uPrime()
                bPrime()
                u()
                b()
                u()
                bPrime()

            if upperTopEdge == ['G', 'R']:
                b()
                uPrime()
                bPrime()
                u2()
                rPrime()
                uPrime()
                r()

            if upperLeftEdge == ['R', 'G']:
                b()
                u()
                bPrime()
            if upperLeftEdge == ['G', 'R']:
                u()
                rPrime()
                u2()
                r()
                u2()
                rPrime()
                u()
                r()
        