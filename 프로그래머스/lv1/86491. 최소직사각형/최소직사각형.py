def solution(sizes):
    answer = 0
    value1 = 0
    value2 = 0
    temp = []
    for _ in sizes:
        temp.extend(_)
    value1 = max(temp)
    
    for size in sizes:
        size.sort()
        if size[0] > value2:
            value2 = size[0]
    return value1*value2