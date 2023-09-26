def solution(sizes):
    value2 = 0
    for size in sizes:
        size.sort()
        if size[0] > value2:
            value2 = size[0]
    return max(max(_) for _ in sizes )*value2