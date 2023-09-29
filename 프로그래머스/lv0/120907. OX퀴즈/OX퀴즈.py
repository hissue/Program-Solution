def solution(quiz):
    answer = []
    for q in quiz:
        temp = q.split(" ")
        if temp[1] == "-":
            answer.append("O" if int(temp[0]) - int(temp[2]) == int(temp[-1]) else "X")
        else:
            answer.append("O" if int(temp[0]) + int(temp[2]) == int(temp[-1]) else "X")
    return answer