function solution(n) {
    let answer = [];
    // for (let i=0; i<n; i++){
    //     answer.push([]);
    //     for (let j=0; j<n; j++){
    //         answer[i].push(0);
    //     }
    // }
    for (let i=0; i<n; i++){
        answer.push(Array(n).fill(0));
    }
    for (let i=0; i<n; i++){
        for (let j=0; j<n; j++){
            if (i===j){
                answer[i][j] = 1;
            }
        }
    }
    return answer;
}