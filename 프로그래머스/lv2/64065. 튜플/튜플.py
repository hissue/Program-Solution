def solution(s):
    answer = []
    s1 = s.lstrip('{').rstrip('}').split('},{')
    for data in s1:
        answer.append(data.split(','))

    answer.sort(key=lambda x : len(x))

    result = []
    for x in answer:
        for y in x:
            temp = int(y)
            if temp not in result:
                result.append(temp)
    return result