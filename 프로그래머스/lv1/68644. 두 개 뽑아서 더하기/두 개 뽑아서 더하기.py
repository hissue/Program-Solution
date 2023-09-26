from itertools import combinations
def solution(numbers):
    answer = []
    for data in list(combinations(numbers,2)):
        answer.append(sum(data))
    return sorted(list(set(answer)))