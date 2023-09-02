function solution(number) {
    let sum = 0;
    number.split('').map((cur) => sum+=parseInt(cur));
    return sum%9;
}