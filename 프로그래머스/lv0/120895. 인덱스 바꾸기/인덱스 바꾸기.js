function solution(my_string, num1, num2) {
    let arr = my_string.split('');
    let strNum1 = my_string[num1];
    let strNum2 = my_string[num2];
    arr.splice(num1,1,strNum2);
    arr.splice(num2,1,strNum1);
    return arr.join('');
}