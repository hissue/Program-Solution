const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const count = parseInt(input[0]);
const data = input[1].split('');
let result = 0;
function solution() {
    let temp='';
    for(let i=0;i<count;i++){
        if (!isNaN(data[i])){
            temp+=data[i];
        }
        else {
            if (temp){
                result += parseInt(temp);
            }
            temp = '';
        }
    }
    if (temp){
        result += parseInt(temp);
    }
    console.log(result);
}

solution();