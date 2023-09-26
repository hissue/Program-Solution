def solution(emergency):
    idx = 1
    answer = [-1 for _ in range(len(emergency))]
    for data in sorted(emergency,reverse=True):
        answer[emergency.index(data)] = idx
        idx+=1
    
    return answer