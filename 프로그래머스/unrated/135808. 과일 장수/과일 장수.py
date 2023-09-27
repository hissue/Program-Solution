def solution(k, m, score):
    answer = 0
    stack = []
    for data in sorted(score,reverse=True):
        stack.append(data)
        if len(stack) == m:
            answer += m*min(stack)
            stack = []
        
            
    return answer