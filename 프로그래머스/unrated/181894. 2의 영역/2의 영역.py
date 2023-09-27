def solution(arr):
    end = 0
    if 2 not in arr:
        return [-1]
    else:
        for idx in range(len(arr)-1,-1,-1):
            if arr[idx] == 2:
                end = idx
                break
        return arr[arr.index(2):len(arr)-arr[::-1].index(2)]