def tenToThree(n):
    result = ""
    while n > 0:
        result+=str(n%3)
        n//=3
    return result

def threeToTen(n):
    answer=0
    for idx in range(len(n)):
        answer+=int(n[idx])*3**(len(n)-idx-1)
    return answer

def solution(n):
    return threeToTen(tenToThree(n))