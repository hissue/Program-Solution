def solution(numlist, n):
    answer = {}
    result = []
    for i in numlist:
        if abs(n-i) not in answer:
            answer[abs(n-i)] = [i]
        else:
            answer[abs(n-i)].append(i)
    
    for data in sorted(list(answer.items())):
        result += sorted(data[1], reverse=True)

    return result