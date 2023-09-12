import sys
def solution(a):
    if a <= 1:
        return 1
    else:
        return a*solution(a-1)

N = int(sys.stdin.readline())
print(solution(N))