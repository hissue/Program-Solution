function solution(a, b, c) {
//     if (a===b && b===c){
//         return (a + b + c)*(a**2 + b**2 + c**2)*(a**3 + b**3 + c**3);
        
//     }else if (a!==b && b!==c && a!==c){
//         return a+b+c;
        
//     }else {
//         return (a + b + c)*(a**2 + b**2 + c**2);
//     }
    let sum1 = a + b + c;
    let sum2 = a**2 + b**2 + c**2;
    let sum3 = a**3 + b**3 + c**3;
    
    if (a===b && b===c){
        return sum1*sum2*sum3;
    }else if (a===b || b===c || a===c) {
        return sum1*sum2;
    }else {
        return sum1;
    }
}