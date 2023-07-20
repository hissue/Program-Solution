function solution(myString) {
    return myString.split('').map((e)=> e === 'a' ? 'A' : e != 'A' ? e.toLowerCase() : e).join('');
}