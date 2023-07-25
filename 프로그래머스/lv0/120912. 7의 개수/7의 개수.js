function solution(array) {
    let answer = '';
    array.map(e=>{
        answer+=e;
    })
    return answer.length - answer.split('7').join('').length;
}