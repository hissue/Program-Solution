def solution(a, b, n):
    answer = 0
    while n >= a:
        glass = (n//a) * b
        n = glass + n%a
        answer+= glass
    return answer