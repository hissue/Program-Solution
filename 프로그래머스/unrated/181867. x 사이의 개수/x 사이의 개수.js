function solution(myString) {
    // let answer = [];
    // let myStringSplit = myString.split('x');
    // for (let i in myStringSplit){
    //     answer.push(myStringSplit[i].length);
    // }
    // return answer;
    return myString.split('x').map((v) => v.length)
}