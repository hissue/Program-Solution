function solution(a, b) {
    let strA = a+'';
    let strB = b+'';
    return Number(strA+strB) > Number(strB+strA) ? Number(strA+strB) : Number(strB+strA);
}