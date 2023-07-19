function solution(slice, n) {
    let answer = 0;
    while ( n > slice*answer){
        answer++;
    }
    return answer;
}