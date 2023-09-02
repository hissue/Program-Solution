function solution(strArr) {
    let answer = [];
    for (let i in strArr){
        if (!strArr[i].includes("ad")){
            answer.push(strArr[i]);
        }
    }
    return answer;
}