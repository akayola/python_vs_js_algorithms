/*
  Count characters
  /[a-z0-9]/ - using regular expression to match alpha-numeric,
  code with regular expression is ~55% slower.
  */

function charCountRE(str) {
    let result = {};
    for (let char of str.toLowerCase()) {
        if (/[a-z,0-9]/.test(char) && char !== ',') {
            if (result[char] > 0) {
                result[char]++;
            } else {
                result[char] = 1;
            }
        }
    }
    return result;
}

console.log(charCountRE("Hello, how are you?:"));