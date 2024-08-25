function charCountAll(str) {
    let result = {};
    for (let i = 0; i < str.length; i++) {
        //let char = str[i];
        let char = str[i].toLowerCase();
        if (result[char] > 0) {
            result[char]++;
        } else {
            result[char] = 1;
        };
    }
    return result;
}

console.log(charCountAll("Hello? How are you?"));