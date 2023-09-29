def solution(l, r):
    result = []
    answer = [str(_) for _ in range(l,r+1)]
    for data in answer:
        if not data.replace("5","").replace("0",""):
            result.append(data)
    return list(map(int,result)) if result else [-1]