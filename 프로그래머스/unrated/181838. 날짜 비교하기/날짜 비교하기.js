function solution(date1, date2) {
    // let flag = 0;
    // for (let i in date1){
    //     if (date1[i] < date2[i]) return 1;
    //     else if(date1[i] > date2[i]) return 0;
    // }
    // return 0;
    
    // return new Date(date1) < new Date(date2) ? 1 : 0;
    return parseInt(date1.join("")) >= parseInt(date2.join("")) ? 0 : 1 ;
    // return 
                                             
}