function solution(before, after) { 
    // let temp = before;
    // for (let i = 0; i < after.length; i++) {
    //     temp = temp.replace(after[i], '');
    // }
    // return temp.length ? 0 : 1;
    return before.split('').sort().join('') === after.split('').sort().join('') ? 1 : 0;
}