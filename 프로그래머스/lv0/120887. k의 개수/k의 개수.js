function solution(i, j, k) {
    let answer = 0;
    let temp;
    for (let n=i; n<=j; n++){
        temp = String(n).split(''); 
        for(let m=0; m<temp.length; m++){
            if(temp[m]===String(k)) answer++;
        }
   }
    return answer;
}