function solution(arr) {
    const minNumber = Math.min(...arr)
    arr.splice(arr.indexOf(minNumber),1);
    return arr.length ? arr : [-1];
}