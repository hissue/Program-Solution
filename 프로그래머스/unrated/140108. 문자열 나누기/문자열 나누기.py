def solution(s):
    match = s[0]
    count = 0
    answer = 0
    length = len(s)
    for idx in range(length):
        if not count:
            match = s[idx]
            answer+=1
            
        if s[idx] == match:
            count+=1    
        else:
            count-=1
            
    return answer