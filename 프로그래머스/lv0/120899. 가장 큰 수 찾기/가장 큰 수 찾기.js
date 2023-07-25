function solution(array) {
    let max_num = [0,0];
    for (let i=0; i<array.length; i++){
        if (max_num[0] < array[i]) max_num = [array[i],i];
    }
    return max_num;
}