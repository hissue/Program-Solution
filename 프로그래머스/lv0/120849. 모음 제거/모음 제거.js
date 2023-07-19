function solution(my_string) {
    if (my_string.match(/[^aeiou]/g)) return my_string.match(/[^aeiou]/g).join('');
    else return '';

}