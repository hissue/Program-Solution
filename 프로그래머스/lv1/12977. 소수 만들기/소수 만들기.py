from itertools import combinations
sosu = [False,False,True] + [True for _ in range(3, 3001)]

def sosuSolution():
    for i in range(2,3001):
        if sosu[i]:
            for j in range(i,3001,i):
                sosu[j] = False  
            sosu[i] = True

def solution(nums):
    answer = 0
    sosuSolution()
    for data in list(combinations(nums,3)):
        total = sum(data)
        if total < 3001 and sosu[total]:
            answer += 1     
        

    return answer