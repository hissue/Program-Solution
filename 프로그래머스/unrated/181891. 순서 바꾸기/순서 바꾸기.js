function solution(num_list, n) {
    let answer = [];
    let temp = num_list.splice(n);
    return [...temp, ...num_list];
}