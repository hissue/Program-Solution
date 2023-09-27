def solution(s):
    result = []
    alpha = [[] for _ in range(26)]
    for i in range(len(s)):
        idx = ord(s[i])%ord("a")
        alpha[idx].append(i)
        if len(alpha[idx])==1:
            result.append(-1)
        else:
            result.append(i-alpha[idx][-2])
            
    return result