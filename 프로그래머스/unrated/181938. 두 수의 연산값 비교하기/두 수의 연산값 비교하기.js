function solution(a, b) {
    let x = Number(String(a)+String(b));
    let y = (2*a*b);
    return x > y ? x : y;
}