from fastapi import FastAPI
from cube import *
from crossSolver import *
from f2lSolver import *
from ollSolver import *
from pllSolver import *

#main commands
app = FastAPI()

@app.get("/")
def root():
    return {"Hello" : "World"}

@app.post("/randomize")
def randomize():
    return {
        "randomMoves" : randomizeCube(), 
        "cubeState" : getCubeState()
    }
@app.post("/solve")
def solve():
    crossSolver()
    f2lSolver()
    ollSolver()
    pllSolver()
    return {
        "solutionMoves" : solutionSequence, 
        "cubeState" : getCubeState()
    }