from collections import Counter
def solution(weights):
    result = 0
    answer = Counter(weights)
    temp = set(weights)

    for w in temp:
        if answer[w] > 1:
            result += answer[w] * (answer[w]-1) // 2
    
    for x in temp:
        if x * (2/4) in weights:
            result += answer[x]*answer[x*(2/4)]
        if x * (2/3) in weights:
            result += answer[x]*answer[x*(2/3)]
        if x * (3/4) in weights:
            result += answer[x]*answer[x*(3/4)]
    return result