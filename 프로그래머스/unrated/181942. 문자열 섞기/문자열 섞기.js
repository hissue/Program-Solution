function solution(str1, str2) {
    let answer = "";
    for (let i in str1){
        answer += str1[i] + str2[i];
    }
    return answer;
}