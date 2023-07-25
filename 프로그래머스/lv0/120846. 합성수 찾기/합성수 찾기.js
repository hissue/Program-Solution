function solution(n) {
    let answer = 0;
    let temp;
    for(let i=1; i<=n; i++){
        temp = 0;
        for (let j=1; j<=i;j++){
            if (i%j===0) temp++;
        }
        if (temp > 2) answer+=1;
    }
    return answer;
}