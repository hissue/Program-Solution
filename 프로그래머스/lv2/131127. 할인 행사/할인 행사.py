def solution(want, number, discount):
    answer = 0
    cnt = 0
    n = len(want)
    for i in range(len(discount)):
        if discount[i] in want:
            j = want.index(discount[i])
            number[j] = number[j] -1    

        if i > 9:
            if discount[i-10] in want:
                number[want.index(discount[i-10])] += 1

        for num in number:
            if num != 0:
                break   
        else: answer += 1

    return answer