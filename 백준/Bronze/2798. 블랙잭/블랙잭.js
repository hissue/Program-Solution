const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const [n, maxData] = input[0].trim().split(" ").map((e) => parseInt(e));
const arr = input[1].split(" ").map((e) => parseInt(e));
const getCombinations = (array, selectNumber) => {
    const results = [];
    if(selectNumber === 1){
        return array.map((element) => [element]);
    }
    array.forEach((fixed, index, origin) => {
        const rest = origin.slice(index+1);
        const combinations = getCombinations(rest, selectNumber - 1);
        const attached = combinations.map((combination) => [fixed, ...combination]);
        results.push(...attached);
    });
    return results;
}

let add = arr => arr.reduce((a, b) => a + b, 0);

let result = 0;

getCombinations(arr, 3).forEach((elem) => {
    let temp = add(elem);
    if (temp <= maxData && temp > result) {
        result = temp;
    }
})

console.log(result);