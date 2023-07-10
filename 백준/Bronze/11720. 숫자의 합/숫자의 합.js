const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const count = parseInt(input[0]);

function solution() {
    const data = input[1].split("");
    let result = 0;
    for(let i=0;i<count;i++){
        result+=parseInt(data[i]);
    }
    console.log(result);
}

solution()