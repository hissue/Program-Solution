function solution(my_string, is_suffix) {
    while (my_string.length >= is_suffix.length){
        if(my_string === is_suffix) return 1;
        my_string = my_string.slice(1);
    }
    return 0;
}