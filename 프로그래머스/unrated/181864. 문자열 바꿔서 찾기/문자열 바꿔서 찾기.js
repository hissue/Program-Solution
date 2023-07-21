function solution(myString, pat) {
    return [...myString].map(elem=> elem==='A' ? 'B':'A').join('').includes(pat) ? 1 :0;
}