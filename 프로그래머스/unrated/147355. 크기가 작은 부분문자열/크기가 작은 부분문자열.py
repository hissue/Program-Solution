def solution(t, p):
    answer = 0
    i=0
    while i < len(t)-len(p)+1:
        if t[i:i+len(p)] <= p:
            answer+=1
        i+=1
    return answer