function factorial(n){
    if (n<=1) return 1; 
    else return factorial(n-1) * n;    
}

function solution(n) {
    let idx = 0;
    while(factorial(idx) <= n) idx++;
    return idx-1;
}