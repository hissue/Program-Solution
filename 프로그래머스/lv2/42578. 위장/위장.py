import sys
from itertools import product
def solution(clothes):
    answer = 1
    type = {}
    for data in clothes:
        if data[1] not in type:
            type[data[1]] = []
        type[data[1]].append(data[0])
    
    for v in type.values():
        answer *= len(v)+1
    
    return answer-1