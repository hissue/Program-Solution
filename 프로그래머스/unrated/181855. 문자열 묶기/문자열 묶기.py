def solution(strArr):
    answer = {}
    for s in strArr:
        length = len(s)
        if length in answer:
            answer[length] +=1
        else:
            answer[length] = 1
            
    return max(answer.values())