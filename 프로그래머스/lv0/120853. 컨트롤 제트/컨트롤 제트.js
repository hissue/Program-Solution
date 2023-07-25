function solution(s) {
    let answer = [];
    s.split(' ').map(e=>{
        e ? (e === 'Z' ? answer.pop() : answer.push(Number(e))) : '';
        
    })
    return answer.length ? answer.reduce((result,e)=> result + e) : 0;
}