const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    let answer = input[0].split('');
    for (let i in answer){
        console.log(answer[i]);
    }
});