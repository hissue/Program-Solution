function solution(arr, delete_list) {
    let answer = [];
    let flag = true;
    for (let i in arr) {
        flag = true;
        for (let j in delete_list) {
            if (arr[i] == delete_list[j]) {
                flag = false;
            }
        }
        if (flag){
            answer.push(arr[i])
        }
    }
    return answer;
}