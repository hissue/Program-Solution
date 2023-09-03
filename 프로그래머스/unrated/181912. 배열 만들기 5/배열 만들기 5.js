function solution(intStrs, k, s, l) {
    let answer = [];
    intStrs.map((v) => {
        let temp = parseInt(v.split("").splice(s,l).join(""));
        if (temp > k) answer.push(temp);
    })
    return answer;
}