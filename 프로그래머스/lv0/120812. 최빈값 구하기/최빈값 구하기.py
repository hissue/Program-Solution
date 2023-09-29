import collections
def solution(array):
    answer = collections.Counter(array)
    m = max(answer.values())
    count = 0
    for k,v in answer.items():
        if  v == m:
            result = k
            count+=1
    return result if count == 1 else -1