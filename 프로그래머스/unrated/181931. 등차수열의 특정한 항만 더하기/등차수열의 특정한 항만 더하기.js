function solution(a, d, included) {
    let answer = 0;
    for (let i in included){
        if (included[i]){
            answer += (a+d*i);
        }
    }
    return answer;
}