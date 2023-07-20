function solution(number, n, m) {
    var answer = 0;
    return !(number%n) && !(number%m) ? 1 : 0;
}