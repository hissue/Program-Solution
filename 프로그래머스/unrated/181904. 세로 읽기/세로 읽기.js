function solution(my_string, m, c) {
    let answer = "";
    // let max_idx = Math.ceil(my_string.length/m);
    // for (let i=0; i<max_idx; i++){
    //     answer+=my_string.split("")[(i*m+(c-1))];
    // }
    for (let i=c-1; i<my_string.length; i+=m) answer+=my_string[i];
    return answer;
}