function solution(n, arr = []) {
    // let answer = [n];
    // while(n!==1){
    //     n = n%2 ? n*3+1 : n/2;
    //     answer.push(n);
    // }
    // return answer;
    
    // 재귀
    arr.push(n);
    if (n===1) return arr;
    if (n%2) return solution(n*3+1,arr); 
    return solution(n/2,arr);
}