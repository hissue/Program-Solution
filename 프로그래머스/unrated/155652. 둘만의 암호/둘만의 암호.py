def solution(s, skip, index):
    answer = []
    result = ""
    for data in range(ord("a"),ord("a")+26):
        if chr(data) not in skip:
            answer.append(chr(data))
    
    for d in s:
        result += answer[(answer.index(d)+index)%len(answer)]
    return result