def solution(num, total):
    answer = [i for i in range(-(total+num),total+num)]
    i = 0
    while sum(answer[i:i+num]) != total:
        i +=1
    return answer[i:i+num]
    