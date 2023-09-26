def solution(array, n):
    answer = 0
    temp = [100,0]
    for data in array:
        temp_abs = abs(n-data)
        if temp[0] == temp_abs:
            temp[0] = temp_abs
            temp[1] = min(temp[1],data)
        elif temp[0] > temp_abs:
            temp[0] = abs(n-data)
            temp[1] = data
        else:
            continue
    return temp[1]