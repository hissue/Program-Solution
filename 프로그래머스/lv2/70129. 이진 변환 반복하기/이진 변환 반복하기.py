def solution(s):
    answer = [0,0]
    while s!="1":
        temp=""
        for _ in s:
            if (_!="0"):
                temp+=_
            else:
                answer[1]+=1
        answer[0]+=1
        s = str(format(len(temp), 'b'))
    return answer