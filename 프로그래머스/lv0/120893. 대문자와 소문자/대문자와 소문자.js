function solution(my_string) {
    let answer = '';
    my_string.split('').map(e=>{
    if (e.toUpperCase() !== e) {
        answer+=e.toUpperCase();
    }else {
        answer+=e.toLowerCase();
    }
    })
    return answer;
}