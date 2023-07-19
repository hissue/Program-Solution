function solution(arr, k) {
    let answer = k % 2 ? arr.map((elem) => {return elem*k}) : arr.map((elem)=>{return elem+k}) ;
    return answer;
}