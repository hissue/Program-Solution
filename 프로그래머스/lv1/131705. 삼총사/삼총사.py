import itertools
def solution(number):
    answer = 0
    for data in list(itertools.combinations(number,3)):
        if not sum(data):
            print(data)
            answer+=1
    return answer