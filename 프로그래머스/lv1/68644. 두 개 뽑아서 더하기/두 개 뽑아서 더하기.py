from itertools import combinations
def solution(numbers):
    answer = []
    for data in list(combinations(numbers,2)):
        temp = sum(data)
        if temp not in answer:
            answer.append(temp)
    return sorted(answer)