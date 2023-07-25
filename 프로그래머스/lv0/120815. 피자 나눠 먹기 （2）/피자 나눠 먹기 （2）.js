function solution(n) {
    let idx = 1;
    while ((6*idx)%n !== 0){
        idx++;
    }
    return idx;
}