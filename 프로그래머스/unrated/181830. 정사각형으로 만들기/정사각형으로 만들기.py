def solution(arr):
    col = len(arr)
    row = len(arr[0])
    length = max(len(arr),len(arr[0]))
    for i in range(col):
        arr[i] += [0] * (length - row)
        
    return arr + [[0 for _ in range(length)]] * (length - col)