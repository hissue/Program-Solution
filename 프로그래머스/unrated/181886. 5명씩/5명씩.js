function solution(names) {
    let answer = names.filter((elem,index)=>{
        return index%5===0;
    })
    return answer;
}