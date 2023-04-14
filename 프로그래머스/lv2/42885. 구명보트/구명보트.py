from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    temp = deque(people)
    while temp:
        if len(temp) == 1:
            answer+=1
            break

        a = temp.popleft()
        b = temp.pop()

        if a+b > limit:
            answer+=1
            temp.insert(0,a)
            continue

        answer+=1

    return answer