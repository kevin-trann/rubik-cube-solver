from cube import *


#updates cube states
(upperTopLeftCorner, upperTopRightCorner, upperBottomLeftCorner, 
upperBottomRightCorner, lowerTopLeftCorner, lowerTopRightCorner,
lowerBottomLeftCorner, lowerBottomRightCorner, upperTopEdge, 
upperLeftEdge, upperRightEdge, upperBottomEdge, backLeftEdge,
backRightEdge, frontLeftEdge, frontRightEdge, lowerTopEdge,
lowerLeftEdge, lowerRightEdge, lowerBottomEdge) = changeCubeState()

#algorithims pre-yellow cross
def IShapeAlg():
    f()
    r()
    u()
    rPrime()
    uPrime()
    fPrime()
    
def LShapeAlg():
    wideF()
    r()
    u()
    rPrime()
    uPrime()
    wideFPrime()

#algorthims post-yellow cross
def antiSuneAlg():
    r()
    u2()
    rPrime()
    uPrime()
    r()
    uPrime()
    rPrime()
    
def suneAlg():
    r()
    u()
    rPrime()
    u()
    r()
    u2()
    rPrime()
    
def hShapeAlg():
    r()
    u()
    rPrime()
    u()
    r()
    uPrime()
    rPrime()
    u()
    r()
    u2()
    rPrime()

def piShapeAlg():
    r()
    u2()
    r2()
    uPrime()
    r2()
    uPrime()
    r2()
    u2()
    r()

def sShapeAlg():
    f()
    rPrime()
    fPrime()
    wideR()
    u()
    r()
    uPrime()
    wideRPrime() 

def TShapeAlg():
    wideR()
    u()
    rPrime()
    uPrime()
    wideRPrime()
    f()
    r()
    fPrime()
    
def UShapeAlg():
    r2()
    d()
    rPrime()
    u2()
    r()
    dPrime()
    rPrime()
    u2()
    rPrime()
    
def ollSolver():
    
    global ollSequence

    #while yellow cross isnt formed ontop
    while cube[0][0][1] != 'Y' or cube[0][1][0] != 'Y' or cube[0][1][2] != 'Y' or cube[0][2][1] != 'Y':
        
        #I-Shape cases
        if cube[0][1][0] == 'Y' and cube[0][1][2] == 'Y':
            IShapeAlg()
            continue
        
        if cube[0][0][1] == 'Y' and cube[0][2][1] == 'Y':
            u()
            IShapeAlg()
            continue
        
        #L-Shape cases
        if cube[0][1][2] == 'Y' and cube[0][2][1] == 'Y':
            LShapeAlg()
            continue
        
        if cube[0][1][0] == 'Y' and cube[0][2][1] == 'Y':
            uPrime()
            LShapeAlg()
            continue
        
        if cube[0][1][0] == 'Y' and cube[0][0][1] == 'Y':
            u2()
            LShapeAlg()
            continue
        
        if cube[0][1][2] == 'Y' and cube[0][0][1] == 'Y':
            u()
            LShapeAlg()
            continue
        
        #dot case
        else:
            IShapeAlg()
            LShapeAlg()
        
    #checks if top is already solved (edge case)
    if cube[0][0] == ['Y', 'Y', 'Y'] and cube[0][1] == ['Y', 'Y', 'Y'] and cube[0][2] == ['Y', 'Y', 'Y']:
        return

    #check for T-shape and U-shape cases
    if cube[0][0][0] == 'Y' and cube[0][0][2] == 'Y':
        
        if cube[1][0][0] == 'Y':
            UShapeAlg()
            
        else:
            u()
            TShapeAlg()
    
    elif cube[0][0][2] == 'Y' and cube[0][2][2] == 'Y':
        
        if cube[1][0][0] == 'Y':
            TShapeAlg()
            
        else:
            uPrime()
            UShapeAlg()
            
    elif cube[0][2][0] == 'Y' and cube[0][2][2] == 'Y':
        
        if cube[4][0][0] == 'Y':
            uPrime()
            TShapeAlg()
            
        else:
            u2()
            UShapeAlg()
            
    elif cube[0][0][0] == 'Y' and cube[0][2][0] == 'Y':
        
        if cube[1][0][2] == 'Y':
            u2()
            TShapeAlg()
            
        else:
            u()
            UShapeAlg()
    
    #check for L-Shape case
    elif cube[0][0][0] == 'Y' and cube[0][2][2] == 'Y':
        
        if cube[1][0][0] == 'Y':
            sShapeAlg()
        
        else:
            u2()
            sShapeAlg()
    
    elif cube[0][0][2] == 'Y' and cube[0][2][0] == 'Y':
        
        if cube[1][0][2] == 'Y': 
            uPrime()
            sShapeAlg()
        
        else:
            u()
            sShapeAlg()
    
    #sune and antisune case
    
    elif cube[0][0][0] == 'Y':
        
        if cube[1][0][2] == 'Y':
            uPrime()
            suneAlg()
        else:
            u()
            antiSuneAlg()
        
    elif cube[0][0][2] == 'Y':
        
        if cube[1][0][2] == 'Y':
            u2()
            suneAlg()
        else:
            antiSuneAlg()
        
    elif cube[0][2][0] == 'Y':
        
        if cube[1][0][2] == 'Y':
            suneAlg()
        else:
            u2()
            antiSuneAlg()
        
    elif cube[0][2][2] == 'Y':
        
        if cube[2][0][2] == 'Y':
            u()
            suneAlg()
        else:
            uPrime()
            antiSuneAlg()
    
    #check for h-shape cases
    
    elif cube[4][0][0] == 'Y' and cube[4][0][2] == 'Y' and cube[2][0][0] == 'Y' and cube[2][0][2] == 'Y':
        hShapeAlg()
        
    elif cube[1][0][0] == 'Y' and cube[1][0][2] == 'Y' and cube[3][0][0] == 'Y' and cube[3][0][2] == 'Y':
        u()
        hShapeAlg()
        
    #check for pi-shape cases
    
    elif cube[4][0][0] == 'Y' and cube[4][0][2] == 'Y':
        piShapeAlg()
        
    elif cube[3][0][0] == 'Y' and cube[3][0][2] == 'Y':
        uPrime()
        piShapeAlg()
        
    elif cube[2][0][0] == 'Y' and cube[2][0][2] == 'Y':
        u2()
        piShapeAlg()
        
    elif cube[1][0][0] == 'Y' and cube[1][0][2] == 'Y':
        u()
        piShapeAlg()
    
    
    #get OLL moves
    recordOLL = False
    
    for move in solutionSequence:
        
        if recordOLL:
            ollSequence.append(move)
        
        if move != 'F2L':
            continue
        else:
            recordOLL = True
    solutionSequence.append("OLL")