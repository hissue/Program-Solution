function solution(arr, flag) {
    let answer = [];
    for (let i in arr){
        if (flag[i]) {
           answer.push(...Array(arr[i]*2).fill(arr[i]));
        }
        else {
            answer.splice(answer.length-arr[i],arr[i])
        }
    }
    return answer;
}