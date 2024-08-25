
function getRandomArbitrary(min, max) {
  return Math.random() * (max - min) + min;
}

//console.log(Math.random())
//#console.log(getRandomArbitrary(0, 10000))

//for (let x = 0; x <= 1000; x++) {
//    console.log(getRandomArbitrary(0.99, 1.01))
//    }

function randomChoice(array) {
    return array[Math.floor(Math.random() * array.length)];
}

console.log(randomChoice([1, 2, 3, 4]));

function calculate_result(x, y, z) {
    return 8 * x ** 3 + 9 * y ** 4 + 89 * z ** 2 - 73;
}

console.log(calculate_result(0.8384425770478793, 0.8248889344145975, 0.8487783028640401));
console.log(calculate_result(0.8531420943133394, 0.8460656406125175, 0.8441520120863392));
