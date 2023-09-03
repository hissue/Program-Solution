function solution(a, d, included) {
    let answer = 0;
    // for (let i in included){
    //     if (included[i]){
    //         answer += (a+d*i);
    //     }
    // }
    
    included.map((v,idx) => {if (v) answer+= (a+d*idx)})
    return answer;
}