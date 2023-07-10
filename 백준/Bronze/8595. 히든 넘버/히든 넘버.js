const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
let regex = new RegExp(/\d{1,6}/g);
let sum = 0;
while (found = regex.exec(input[1])) {
    sum += parseInt(found[0], 10);
}
console.log(sum);