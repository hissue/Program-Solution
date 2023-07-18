const input = parseInt(require("fs").readFileSync("/dev/stdin").toString().trim());

function sumDigits(n) {
    let sum = 0;
    while (n > 0) {
        sum += n % 10;
        n = Math.floor(n / 10);
    }
    return sum;
}

let result = 0;

for (let i = Math.max(1, input - 60); i < input; i++) {
    if (sumDigits(i) + i === input) {
        result = i;
        break;
    }
}

console.log(result);