def solution(s):
    str_tuples = s[1:-1]
    idx = 0
    temp = ''
    data = []
    for st in str_tuples:
        if st == '{':
            continue
        elif st == '}':
            if temp[0] == ',':
                temp = temp[1:]
            data.append(temp.split(','))
            idx +=1
            temp =''
        else:
            temp += st

    
    data.sort(key=lambda x : len(x))
    answer = []  

    for x in data:
        for d in x:
            temp = int(d)
            if temp not in answer:
                answer.append(temp)
            

    return answer

