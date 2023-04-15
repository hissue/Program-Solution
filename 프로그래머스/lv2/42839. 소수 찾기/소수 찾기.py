from itertools import permutations
def sosu(data):
    for i in range(2,data):
        if data%i == 0:
            return 0
    return 1 

def solution(numbers):
    answer = 0
    dp = [0,1]
    results = []
    for i in range(1,len(numbers)+1):
        results.extend(list(map(list,permutations(numbers,i))))
    

    for result in results:
        x = int("".join(result))
        if x not in dp and sosu(x):
            dp.append(x)
            answer+=1 

    return answer