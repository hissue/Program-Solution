def solution(myStr):
    answer = []
    temp = myStr.replace("a","0").replace("b","0").replace("c","0").split("0")
    for t in temp:
        if t:
            answer.append(t)
    return answer if answer else ["EMPTY"]