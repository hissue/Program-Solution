def solution(arr):
    if len(arr) == 1:
        answer = 0
    else:
        for n in range(1,11):
            if 2**(n-1) < len(arr) and len(arr) <= 2**n:
                answer = n
                break
            
    for i in range((2**answer)-len(arr)):
        arr.append(0)
        
    return arr