function solution(array) {
    // let answer = '';
    // array.map(e=>{
    //     answer+=e;
    // })
    // return answer.length - answer.split('7').join('').length;
    return array.join('').split('7').length -1 ;
}