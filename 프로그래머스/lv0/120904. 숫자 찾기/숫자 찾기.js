function solution(num, k) {
    let answer = String(num).split('').indexOf(String(k))+1;
    return answer ? answer : -1;
}