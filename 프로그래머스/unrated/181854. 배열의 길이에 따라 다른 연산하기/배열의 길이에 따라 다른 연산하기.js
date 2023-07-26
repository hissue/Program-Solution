function solution(arr, n) {
    let answer;
    if (arr.length%2 === 1){
       answer = arr.map((e,index)=> index%2 === 0 ? e+n : e); 
    }
    else {
       answer = arr.map((e,index)=> index%2 === 1 ? e+n : e); 
    }
    return answer;
}