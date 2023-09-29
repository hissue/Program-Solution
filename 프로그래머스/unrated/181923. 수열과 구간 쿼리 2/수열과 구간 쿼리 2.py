def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        temp = 1000001
        for i in range(s,e+1):
            if arr[i] > k and arr[i] < temp:
                temp = arr[i]
        answer.append(-1) if temp == 1000001 else answer.append(temp)
    return answer