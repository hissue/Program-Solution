def solution(numbers, k):
    answer = 0
    count = 0
    length = len(numbers)
    while count != k-1:
        count+=1
        answer = (answer+2)%length
    return answer+1