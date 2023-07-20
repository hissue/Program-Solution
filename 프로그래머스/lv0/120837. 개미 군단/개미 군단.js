function solution(hp) {
    let ate_hp = [5,3,1];
    let idx=0;
    let answer = 0;
    while(hp){
        answer += Math.floor(hp/ate_hp[idx]);
        hp %= ate_hp[idx];
        idx++;
    }
    return answer;
}