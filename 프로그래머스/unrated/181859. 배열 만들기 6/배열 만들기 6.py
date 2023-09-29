def solution(arr):
    stk = []
    i = 0
    length = len(arr)
    while i < length:
        if not stk:
            stk.append(arr[i])
        else:
            if stk[-1] == arr[i]:
                stk.pop()
            else:
                stk.append(arr[i])
        i+=1
    return [-1] if not len(stk) else stk