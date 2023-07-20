function solution(num_str) {
    let answer = 0;
    num_str.split('').map(e=> answer+=parseInt(e));
    return answer;
}