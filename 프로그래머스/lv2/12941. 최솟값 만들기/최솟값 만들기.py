def solution(A,B):
    answer = 0

    A.sort()
    B.sort()
    for i in range(len(A)):
        temp = A.pop(0) * B.pop()
        print(temp)
        answer += temp
    return answer