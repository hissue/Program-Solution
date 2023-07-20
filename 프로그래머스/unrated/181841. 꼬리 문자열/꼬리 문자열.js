function solution(str_list, ex) {
    let answer = str_list.filter((e)=> !e.includes(ex)).join('');
    return answer;
}