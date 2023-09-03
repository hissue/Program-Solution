function solution(numLog) {
    let answer = '';
    let temp = numLog[0];
    for (let i=1 ; i<numLog.length; i++){
        if (numLog[i] == temp + 1){
            answer+="w";
            temp +=1
        }else if(numLog[i] == temp - 1){
            answer+="s";
            temp-=1;
        }else if(numLog[i] == temp + 10){
            answer+="d";
            temp+=10;
        }else{
            answer+="a";
            temp-=10;
        }
    }
    return answer;
}