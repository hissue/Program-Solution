function solution(my_string, m, c) {
    let answer = "";
    for (let i=0; i<Math.ceil(my_string.length/m); i++){
        answer+=my_string.split("")[(i*m+(c-1))];
    }
    return answer;
}