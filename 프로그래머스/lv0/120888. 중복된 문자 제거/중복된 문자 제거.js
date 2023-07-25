function solution(my_string) {
    let answer = my_string.split('');
    for (let i=0;i<my_string.length;i++){
        for (let j=i+1; j<my_string.length;j++){
            if (my_string[i] === my_string[j]) answer.splice(j,1,'');
        }
    }
    return answer.join('');
}