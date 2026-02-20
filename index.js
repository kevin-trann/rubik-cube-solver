randomAlg = "z2 y2 "


async function fetchRandomizeSequence(){

    try{
        const response = await fetch("http://localhost:8000/randomize",{method: "POST"})

        if(!response.ok){
            throw new Error("Could not fetch data")
        }

        const data = await response.json();
        randomMoveSet = data.randomMoves;

        randomAlg = "z2 y2 "

        for(let i = 0; i < randomMoveSet.length;i++){
            randomAlg += randomMoveSet[i] + " ";
        }

        console.log(randomAlg)
        document.getElementById("cube").alg = randomAlg;
        document.getElementById("cube").tempoScale = 3;
    }
    catch(error){
        console.error(error)
    }

}

async function postSolveCube(){
    const response = await fetch("http://localhost:8000/solve", {
        method: "POST"
    });
}

async function fetchSolveSequence(){

    try{
        const response = await fetch("http://localhost:8000/algorithms",{method: "GET"})

        if(!response.ok){
            throw new Error("Could not fetch data")
        }

        const data = await response.json();
        solutionMoveSet = data.solutionMoves;
        solutionAlg = ""

        for(let i = 0; i < solutionMoveSet.length;i++){
            if (solutionMoveSet[i] == 'C' || solutionMoveSet[i] == 'F2L' || solutionMoveSet[i] == 'OLL'){
                continue;
            }
            solutionAlg += solutionMoveSet[i] + " ";
        }

        document.getElementById("cube").experimentalSetupAlg = randomAlg;
        document.getElementById("cube").alg = solutionAlg;
        document.getElementById("cube").tempoScale = 3;
    }
    catch(error){
        console.error(error)
    }

}

async function randomizeAndSolve(){
    await fetchRandomizeSequence();
    await postSolveCube();
}

async function fetchCrossSequence(){

    try{
        const response = await fetch("http://localhost:8000/algorithms",{method: "GET"})

        if(!response.ok){
            throw new Error("Could not fetch data")
        }

        const data = await response.json();
        solutionMoveSet = data.crossMoves;
        solutionAlg = ""

        for(let i = 0; i < solutionMoveSet.length;i++){
            solutionAlg += solutionMoveSet[i] + " ";
        }

        document.getElementById("cube").experimentalSetupAlg = randomAlg;
        document.getElementById("cube").alg = solutionAlg;
        document.getElementById("cube").tempoScale = 3;
    }
    catch(error){
        console.error(error)
    }

}

async function fetchF2LSequence(){

    try{
        const response = await fetch("http://localhost:8000/algorithms",{method: "GET"})

        if(!response.ok){
            throw new Error("Could not fetch data")
        }

        setupAlg = "z2 y2 ";

        const data = await response.json();
        randomMoveSet = data.randomMoves;
        crossMoveSet = data.crossMoves;
        f2LMoveSet = data.f2lMoves;
        solutionAlg = ""

        for(let i = 0; i < randomMoveSet.length;i++){
            setupAlg += randomMoveSet[i] + " ";
        }

        for(let i = 0; i < crossMoveSet.length;i++){
            setupAlg += crossMoveSet[i] + " ";
        }

        for(let i = 0; i < f2LMoveSet.length;i++){
            solutionAlg += f2LMoveSet[i] + " ";
        }

        document.getElementById("cube").experimentalSetupAlg = setupAlg;
        document.getElementById("cube").alg = solutionAlg;
        document.getElementById("cube").tempoScale = 3;
    }
    catch(error){
        console.error(error)
    }

}

async function fetchOLLSequence(){

    try{
        const response = await fetch("http://localhost:8000/algorithms",{method: "GET"})

        if(!response.ok){
            throw new Error("Could not fetch data")
        }

        setupAlg = "z2 y2 ";

        const data = await response.json();
        randomMoveSet = data.randomMoves;
        crossMoveSet = data.crossMoves;
        f2LMoveSet = data.f2lMoves;
        OLLMoveSet = data.ollMoves;
        solutionAlg = ""

        for(let i = 0; i < randomMoveSet.length;i++){
            setupAlg += randomMoveSet[i] + " ";
        }

        for(let i = 0; i < crossMoveSet.length;i++){
            setupAlg += crossMoveSet[i] + " ";
        }

        for(let i = 0; i < f2LMoveSet.length;i++){
            setupAlg += f2LMoveSet[i] + " ";
        }

        for(let i = 0; i < OLLMoveSet.length;i++){
            solutionAlg += OLLMoveSet[i] + " ";
        }

        document.getElementById("cube").experimentalSetupAlg = setupAlg;
        document.getElementById("cube").alg = solutionAlg;
        document.getElementById("cube").tempoScale = 3;
    }
    catch(error){
        console.error(error)
    }

}

async function fetchPLLSequence(){

    try{
        const response = await fetch("http://localhost:8000/algorithms",{method: "GET"})

        if(!response.ok){
            throw new Error("Could not fetch data")
        }

        setupAlg = "z2 y2 ";

        const data = await response.json();
        randomMoveSet = data.randomMoves;
        crossMoveSet = data.crossMoves;
        f2LMoveSet = data.f2lMoves;
        OLLMoveSet = data.ollMoves;
        PLLMoveSet = data.pllMoves;
        solutionAlg = ""

        for(let i = 0; i < randomMoveSet.length;i++){
            setupAlg += randomMoveSet[i] + " ";
        }

        for(let i = 0; i < crossMoveSet.length;i++){
            setupAlg += crossMoveSet[i] + " ";
        }

        for(let i = 0; i < f2LMoveSet.length;i++){
            setupAlg += f2LMoveSet[i] + " ";
        }

        for(let i = 0; i < OLLMoveSet.length;i++){
            setupAlg += OLLMoveSet[i] + " ";
        }

        for(let i = 0; i < PLLMoveSet.length;i++){
            solutionAlg += PLLMoveSet[i] + " ";
        }

        document.getElementById("cube").experimentalSetupAlg = setupAlg;
        document.getElementById("cube").alg = solutionAlg;
        document.getElementById("cube").tempoScale = 3;
    }
    catch(error){
        console.error(error)
    }

}


