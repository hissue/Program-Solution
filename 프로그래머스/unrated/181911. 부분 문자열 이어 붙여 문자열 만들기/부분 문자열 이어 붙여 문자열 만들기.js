function solution(my_strings, parts) {
    var answer = '';
    for (let i in my_strings){
        answer+=my_strings[i].split('').splice(parts[i][0],parts[i][1]-parts[i][0]+1).join('');
    }
    return answer;
}