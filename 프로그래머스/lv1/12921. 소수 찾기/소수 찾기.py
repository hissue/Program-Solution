sosu = [False,False,True] + [True for _ in range(3, 1000001)]

def sosuSolution():
    for i in range(2,1000001):
        if sosu[i]:
            for j in range(i,1000001,i):
                sosu[j] = False  
            sosu[i] = True

def solution(n):
    answer = 0
    sosuSolution()
    for i in range(2,n+1):
        if sosu[i]:
            answer+=1
    return answer