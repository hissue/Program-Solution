def solution(s):
    answer = ""
    alpha = [0 for _ in range(26)]
    for alp in s:
        alpha[ord(alp)%ord("a")]+=1
    for idx in range(26):
        if alpha[idx] == 1:
            answer+=chr(ord("a")+idx)
    return answer