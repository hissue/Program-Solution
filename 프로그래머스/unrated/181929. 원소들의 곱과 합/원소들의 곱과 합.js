function solution(num_list) {
    let allSum = num_list.reduce((arr, e) => arr+e);
    let allMul = num_list.reduce((arr,e)=> arr*e);
    return allMul < allSum**2 ? 1 : 0;
}