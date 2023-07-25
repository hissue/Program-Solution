function solution(numbers) {
    // let max_num = -100000000;
    // for (let i=0; i<numbers.length; i++){
    //     for (let j=i+1; j<numbers.length;j++){
    //         if (max_num < numbers[i]*numbers[j]){
    //             max_num = numbers[i]*numbers[j];
    //         }
    //     }
    // }
    numbers.sort((a,b)=>a-b);
    return Math.max(numbers[0]*numbers[1],numbers[numbers.length-1]*numbers[numbers.length-2])
}