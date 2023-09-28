def solution(arr):
    stk = []
    i = 0
    length = len(arr)
    while i < length:
        if not stk:
            stk.append(arr[i])
            i+=1
        else:
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i+=1
            else:
                stk.pop()
    return stk