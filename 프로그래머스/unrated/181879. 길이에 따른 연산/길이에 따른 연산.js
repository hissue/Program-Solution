function solution(num_list) {
    let answer = num_list.length >= 11 ? num_list.reduce((arr,e)=> arr+e) : num_list.reduce((arr,e) => arr*e)
    return answer;
}