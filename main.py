from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from cube import *
from crossSolver import *
from f2lSolver import *
from ollSolver import *
from pllSolver import *

#main commands
randomizeCube()
crossSolver()
f2lSolver()
ollSolver()
pllSolver()
printCube()
print(scrambleSequence)
print("")
print(crossSequence)
print("")
print(f2lSequence)
print("")
print(ollSequence)
print("")
print(pllSequence)
print("")
print(solutionSequence)

app = FastAPI()

@app.get("/")
def root():
    return {"Hello" : "World"}

@app.post("/randomize")
def randomize():
    randomizeCube()
    return {
        "randomMoves" : scrambleSequence
    }
@app.post("/solve")
def solve():
    crossSolver()
    f2lSolver()
    ollSolver()
    pllSolver()

@app.get("/algorithms")
def getAlgorithms():
    return {
        "solutionMoves" : solutionSequence, 
        "crossMoves" : crossSequence,
        "f2lMoves" : f2lSequence,
        "ollMoves" : ollSequence,
        "pllMoves" : pllSequence,
        "randomMoves" : scrambleSequence
    }
    

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)