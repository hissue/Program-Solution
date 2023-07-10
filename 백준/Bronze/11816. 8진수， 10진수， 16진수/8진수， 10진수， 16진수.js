const input = require('fs').readFileSync('/dev/stdin').toString().split('');
function hex(data) {
    console.log(parseInt(data.join(''), 16));
}

function oct(data) {
    console.log(parseInt(data.join(''), 8));
}

function solution() {
    // 16진수인 경우
    if (input[0]+input[1] === "0x"){
        hex(input.slice(2,));
    }
    // 8진수인 경우
    else if (input[0] === "0") {
        oct(input.slice(1,));
    }
    // 10진수인 경우
    else {
        console.log(parseInt(input.join('')));
    }
}

solution()