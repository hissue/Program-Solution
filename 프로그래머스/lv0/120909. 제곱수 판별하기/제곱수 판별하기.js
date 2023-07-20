function solution(n) {
    let answer = Math.sqrt(n);
    // return parseInt(answer) === answer ? 1 : 2;
    return Number.isInteger(answer) ? 1 : 2;
    
}