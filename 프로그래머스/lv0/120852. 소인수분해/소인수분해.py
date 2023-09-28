def solution(n):
    answer = []
    idx = 2
    while n!=1:
        if not n%idx:
            answer.append(idx)
            n //=idx
        else:
            idx+=1
    return sorted(list(set(answer)))