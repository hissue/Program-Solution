from collections import deque
def solution(priorities, location):
    answer = 0
    temp = deque()
    for i in range(len(priorities)):
        temp.append([i,priorities[i]])

    # 뒤에꺼 다 봤는데 우선 순위가 더 높은게 있다면 다시 넣는다.
    # 우선 순위 높은게 없다면 뺀다.
    while temp:
        I,J = temp.popleft()
        flag = 1
        for prioritie in temp:
            if J < prioritie[1]:
                temp.append([I,J])
                flag=0
                break

        if flag:
            answer+=1
            
        if I == location and flag:
            return answer