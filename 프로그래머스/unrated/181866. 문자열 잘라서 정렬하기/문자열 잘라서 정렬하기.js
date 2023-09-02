function solution(myString) {
    let temp = [];
    let answer = myString.split("x");
    for (let i in answer){
        if (!answer[i] == ""){
            temp.push(answer[i])
        }
    }
    return temp.sort();
}