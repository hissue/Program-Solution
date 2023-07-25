function solution(numbers) {
    let max_num = -100000000;
    for (let i=0; i<numbers.length; i++){
        for (let j=i+1; j<numbers.length;j++){
            if (max_num < numbers[i]*numbers[j]){
                max_num = numbers[i]*numbers[j];
            }
        }
    }
    return max_num;
}