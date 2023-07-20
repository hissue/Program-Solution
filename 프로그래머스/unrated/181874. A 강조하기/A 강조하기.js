function solution(myString) {
    // return myString.split('').map((e)=> e === 'a' ? 'A' : e != 'A' ? e.toLowerCase() : e).join('');
    return myString.toLowerCase().replaceAll('a','A')
}