function solution(num_str) {
    return num_str.split('').reduce((arr,e) => arr+Number(e),0);
}