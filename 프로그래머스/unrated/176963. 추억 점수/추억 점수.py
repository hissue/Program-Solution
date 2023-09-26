def solution(name, yearning, photo):
    answer = []
    for pht in photo:
        temp = 0
        for p in pht:
            if p in name:
                temp +=yearning[name.index(p)]
        answer.append(temp)
    return answer