randomAlg = "z2 y2 "

async function fetchRandomizeSequence(){

    try{
        const response = await fetch("http://localhost:8000/randomize",{method: "POST"})

        if(!response.ok){
            throw new Error("Could not fetch data")
        }

        const data = await response.json();
        randomMoveSet = data.randomMoves["Scramble Sequence"];

        randomAlg = "z2 y2 "

        for(let i = 0; i < randomMoveSet.length;i++){
            randomAlg += randomMoveSet[i] + " ";
        }

        console.log(randomAlg)
        document.getElementById("cube").alg = randomAlg;
    }
    catch(error){
        console.error(error)
    }

}

async function fetchSolveSequence(){

    try{
        const response = await fetch("http://localhost:8000/solve",{method: "POST"})

        if(!response.ok){
            throw new Error("Could not fetch data")
        }

        const data = await response.json();
        solutionMoveSet = data.solutionMoves;
        solutionAlg = ""

        for(let i = 0; i < solutionMoveSet.length;i++){
            solutionAlg += solutionMoveSet[i] + " ";
        }

        console.log(solutionAlg)

        document.getElementById("cube").experimentalSetupAlg = randomAlg;
        document.getElementById("cube").alg = solutionAlg;
    }
    catch(error){
        console.error(error)
    }

}