from cube import *

def diagnoalAlg():
    f()
    r()
    uPrime()
    rPrime()
    uPrime()
    r()
    u()
    rPrime()
    fPrime()
    r()
    u()
    rPrime()
    uPrime()
    rPrime()
    f()
    r()
    fPrime()

def headLightsAlg():
    r()
    u()
    rPrime()
    uPrime()
    rPrime()
    f()
    r2()
    uPrime()
    rPrime()
    uPrime()
    r()
    u()
    rPrime()
    fPrime()

def hAlg():
    m2()
    u()
    m2()
    u2()
    m2()
    u()
    m2()

def uAAlg():
    r()
    uPrime()
    r()
    u()
    r()
    u()
    r()
    uPrime()
    rPrime()
    uPrime()
    r2()
    
def uBAlg():
    r2()
    u()
    r()
    u()
    rPrime()
    uPrime()
    rPrime()
    uPrime()
    rPrime()
    u()
    rPrime()

def zAlg():
    mPrime()
    u()
    m2()
    u()
    m2()
    u()
    mPrime()
    u2()
    m2()

def pllSolver():
    global pllSequence
    while not (cube[1][0][0] == cube [1][0][1] == cube [1][0][2]) or not (cube[2][0][0] == cube [2][0][1] == cube [2][0][2]) or not (cube[3][0][0] == cube [3][0][1] == cube [3][0][2]) or not (cube[4][0][0] == cube [4][0][1] == cube [4][0][2]):
        
        #check for uA and uB by checking for top row of same pieces and headlights all around
        
        #base case (same matching top row at back and headlights all around)
        if cube[3][0][0] == cube[3][0][1] == cube[3][0][2] and cube[1][0][0] == cube[1][0][2] and cube[2][0][0] == cube[2][0][2] and cube[4][0][0] == cube[4][0][2]:
            
            if cube[1][0][1] == cube[2][0][0]:
                uAAlg()
                
            else:
                uBAlg()
        
        elif cube[2][0][0] == cube[2][0][1] == cube[2][0][2] and cube[1][0][0] == cube[1][0][2] and cube[3][0][0] == cube[3][0][2] and cube[4][0][0] == cube[4][0][2]:
            uPrime()
            continue
        
        elif cube[1][0][0] == cube[1][0][1] == cube[1][0][2] and cube[3][0][0] == cube[3][0][2] and cube[2][0][0] == cube[2][0][2] and cube[4][0][0] == cube[4][0][2]:
            u2()
            continue
        
        elif cube[4][0][0] == cube[4][0][1] == cube[4][0][2] and cube[1][0][0] == cube[1][0][2] and cube[2][0][0] == cube[2][0][2] and cube[3][0][0] == cube[3][0][2]:
            u()
            continue
        
        #check for h and z cases by checking for headlights all around
        elif cube[3][0][0] == cube[3][0][2] and cube[1][0][0] == cube[1][0][2] and cube[2][0][0] == cube[2][0][2] and cube[4][0][0] == cube[4][0][2]:
            
            #hCase
            if cube[1][0][1] == cube[3][0][0]:
                hAlg()
            
            #zCase
            else:
                
                if cube[1][0][1] == cube[2][0][0]:
                    u()
                    zAlg()
                else:
                    zAlg()
        
        #cases must be first-step pll (headlights or diagnoal)
        
        #headlights cases
        
        elif cube[4][0][0] == cube[4][0][2]:
            headLightsAlg()
            
        elif cube[1][0][0] == cube[1][0][2]:
            u()
            headLightsAlg()
            
        elif cube[2][0][0] == cube[2][0][2]:
            u2()
            headLightsAlg()
            
        elif cube[3][0][0] == cube[3][0][2]:
            uPrime()
            headLightsAlg()
        
        #diagnoal case
        else:
            diagnoalAlg()
    
    #top row pieces now same on every side; use u moves to align and solve
    if cube[1][0][0] == 'R':
        uPrime()
    
    elif cube[1][0][0] == 'G':
        u2()
        
    elif cube[1][0][0] == 'O':
        u()
    
    #get PLL moves
    recordPLL = False
    
    for move in solutionSequence:
        
        if recordPLL:
            pllSequence.append(move)
        
        if move != 'OLL':
            continue
        else:
            recordPLL = True
    