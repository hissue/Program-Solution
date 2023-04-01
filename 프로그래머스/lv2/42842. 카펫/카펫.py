def solution(brown, yellow):
    arr = []
    answer = []

    #col,row
    for i in range(1,yellow+1):
        arr.append([i,yellow//i])

    for c,r in arr:
        if r > c:
            continue
        
        if (c+2)*(r+2)  == yellow + brown:
            answer.append([c+2,r+2])

    return answer[0]