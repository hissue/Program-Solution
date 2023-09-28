def solution(arr, k):
    stack = []
    idx = 0
    length = len(arr)
    while len(stack) < k and idx < length:    
        if arr[idx] not in stack:
            stack.append(arr[idx])
        idx+=1
    for idx in range(k-len(stack)):
        stack.append(-1)
    return stack