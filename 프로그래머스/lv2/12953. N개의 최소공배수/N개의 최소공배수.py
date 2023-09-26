def solution(arr):
    answer = 1
    count = 0
    while 1:
        for data in arr:
            if not answer % data:
                count+=1
                
        if count == len(arr):
            break
            
        else:
            count = 0
            answer+=1
            
    return answer