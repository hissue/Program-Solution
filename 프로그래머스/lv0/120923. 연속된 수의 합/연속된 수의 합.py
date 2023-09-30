def solution(num, total):
    answer = [i for i in range(-(total+num),total+num)]
    idx = 0
    for i in range(len(answer)-num+1):
        if sum(answer[i:i+num]) == total:
            idx = i
            break
    return answer[idx:idx+num]
    