function solution(my_string, index_list) {
    let answer = [];
    index_list.map((e) => answer += my_string[e]);
    return answer;
}