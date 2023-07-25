function solution(my_string) {
    let answer = 0;
    my_string.split(/[A-z]/g).map(e=> e ? answer+=Number(e) : 0);
    return answer;
}