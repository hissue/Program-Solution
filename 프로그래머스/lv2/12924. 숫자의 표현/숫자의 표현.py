from collections import deque
def solution(n):
    queue = deque()
    answer=0
    i=1
    while i <= n:
        total = sum(queue)
        if total > n:
            queue.popleft()
        else:
            if total == n:
                answer += 1
            queue.append(i)
            i+=1
            
    return answer+1