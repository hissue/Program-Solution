function solution(numbers) {
    numbers.sort((a,b)=> {
        return a-b;
    }).reverse();
    
    return numbers[0] * numbers[1];
}