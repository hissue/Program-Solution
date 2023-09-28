def solution(arr):
    count = 0
    before = [ 0 * len(arr)]
    while before != arr:
        count+=1
        before = [ _ for _ in arr]
        for idx, data in enumerate(arr):
            if data >= 50 and not data%2:
                arr[idx] = data//2
            elif data < 50 and data%2:
                arr[idx] = data*2+1
        
    return count-1