def solution(n):
    answer = [0]
    idx = 1
    while len(answer) < n+1:
        if idx%3 and "3" not in str(idx):
            answer.append(idx)
        idx+=1
    return answer[-1]