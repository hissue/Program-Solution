function solution(n_str) {
    let idx;
    for (idx=0; idx<n_str.length; idx++) {
        if (n_str[idx] !== '0') break;
    }
    return n_str.slice(idx);
} 