function solution(order) {
    // let temp = String(order).split('');
    // let answer = 0;
    // for (let i=0; i<temp.length; i++){
    //     if (temp[i]==='3' || temp[i]==='6' || temp[i]==='9'){
    //         answer++;
    //     }
    // }
    // return answer;
    return (''+order).split(/[369]/).length-1;
}
