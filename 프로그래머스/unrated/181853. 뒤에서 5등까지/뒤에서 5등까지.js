function solution(num_list) {
    let answer = num_list.sort((a,b) => {return a-b}).slice(0,5)
    return answer;
}