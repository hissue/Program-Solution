function solution(num_list) {
    let answer = [0,0];
    for(let idx in num_list) {
        if (num_list[idx]%2) answer[1]++;
        else answer[0]++;
    }
    
    
    return answer;
}