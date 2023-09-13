def solution(arr, idx):
    min_idx = len(arr)
    for i in range(idx,len(arr)):
        if arr[i] and i < min_idx:
            min_idx = i
    return min_idx if min_idx != len(arr) else -1