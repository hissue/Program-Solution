function solution(num_list) {
    let answer = 0;
    num_list.map((v)=>{
        while(v!==1){
            if (v%2===0){
                v/=2;
            }else{
                v=(v-1)/2;
            }
            answer++;
        }
    })
    
    return answer;
}