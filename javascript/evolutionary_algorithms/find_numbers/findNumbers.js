/*
  Math.random() - static method returns a floating-point,
  pseudo-random number that's greater than or equal to 0 and less than 1.
*/


function getRandomArbitrary(min, max) {
    return Math.random() * (max - min) + min;
}

function randomChoice(array) {
    return array[Math.floor(Math.random() * array.length)];
}

function calculateResult(x, y, z) {
    return 8 * x ** 3 + 9 * y ** 4 + 89 * z ** 2 - 73;
}

function getRank(x, y, z) {
    let answer = calculateResult(x, y, z);
    if (answer === 0) {
        return 99999;
    } else {
        return Math.abs( 1 / answer);
    }
}

let solutions = [];
for (let i = 0; i <= 10000; i++) {
    solutions.push([getRandomArbitrary(0, 10000),
                    getRandomArbitrary(0, 10000),
                    getRandomArbitrary(0, 10000)]);
}

for (let i = 0; i <= 10000; i++) {
    let ranked_solutions = [];
    for (let s of solutions) {
        ranked_solutions.push([getRank(s[0], s[1], s[2]), s]);
    }
    ranked_solutions.sort();
    ranked_solutions.reverse();
    
    console.log("=== generate", i,  "best solutions ===");
    console.log(ranked_solutions[0]);

    if (ranked_solutions[0][0] >= 999) {
        break;
    }

    let best_solutions = ranked_solutions.slice(0, 100);

    let survivors = [];
    let midway = Math.floor(ranked_solutions.length / 2);
    
    for (let i = 0; i <= midway; i++) {
        if (ranked_solutions[i][0] > ranked_solutions[i + midway][0]) {
            survivors.push([ranked_solutions[i][1][0],
                            ranked_solutions[i][1][1],
                            ranked_solutions[i][1][2]]);
        }
    }

    let offspring = [];
    let midway1 = Math.floor(survivors.length / 2);
    for (let i = 0; i <= midway1; i++) {
        let parent_a = survivors[i];
        let parent_b = survivors[i + midway1];
        offspring.push(parent_a);
        offspring.push(parent_b);
    }

    let new_generation = [];
    for (let i = 0; i <= 1000; i++) {
        let element1 = randomChoice(offspring[0]) * getRandomArbitrary(0.99, 1.01);
        let element2 = randomChoice(offspring[1]) * getRandomArbitrary(0.99, 1.01);
        let element3 = randomChoice(offspring[2]) * getRandomArbitrary(0.99, 1.01);

        new_generation.push([element1, element2, element3]);
    }

    solutions = new_generation;
}


//console.log(solutions);

//console.log(getRank(0.1, 0.002, 0.0041));
