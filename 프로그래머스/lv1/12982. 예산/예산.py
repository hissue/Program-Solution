def solution(d, budget):
    d.sort()
    answer = 0
    for i in range(1,len(d)+1):
        if sum(d[:i]) > budget:
            return i-1
    return i