def solution(arr):
    start = 0
    end = 0
    if 2 not in arr:
        return [-1]
    else:
        for idx in range(len(arr)):
            if arr[idx] == 2:
                start = idx
                break
        for idx in range(len(arr)-1,-1,-1):
            if arr[idx] == 2:
                end = idx
                break
        return arr[start:end+1]