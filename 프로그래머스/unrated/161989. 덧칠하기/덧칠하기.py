def solution(n, m, section):
    answer = [True for _ in range(n)]
    count = 0
    
    for idx in section:
        answer[idx-1] = False
    
    for i in section:
        if not answer[i-1]:
            for j in range(i-1, i+m-1):
                if j < n:
                    answer[j] = True
            count+=1
                
    return count