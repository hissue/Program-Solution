def solution(rank, attendance):
    answer = []
    r = 1
    while len(answer) < 3:
        if attendance[rank.index(r)]:
            answer.append(rank.index(r))
        r+=1    
    return 10000 * answer[0] + 100 * answer[1] + answer[2]