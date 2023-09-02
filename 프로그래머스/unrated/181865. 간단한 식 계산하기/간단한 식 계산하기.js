function solution(binomial) {
    let temp = binomial.split(' ');
    if (temp[1] == '+'){
        return parseInt(temp[0]) + parseInt(temp[2]);
    }else if (temp[1] == '-'){
        return parseInt(temp[0]) - parseInt(temp[2]);
    }else {
        return parseInt(temp[0]) * parseInt(temp[2]);
    }
    
}