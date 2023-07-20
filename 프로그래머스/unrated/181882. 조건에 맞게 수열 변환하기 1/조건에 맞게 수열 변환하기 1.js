function solution(arr) {
    let answer = [];
    for (let index in arr) {
        if (arr[index]>=50 && !(arr[index]%2)) answer.push(arr[index]/2);
        else if (arr[index]<50 && arr[index]%2) answer.push(arr[index]*2);
        else answer.push(arr[index]);
    }
    return answer;
}