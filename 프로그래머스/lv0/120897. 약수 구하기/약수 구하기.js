function solution(n) {
    let answer = [];
    for (let i=1; i<=n; i++){
        if (n%i) continue;
        answer.push(i);
    }
    return answer;
}