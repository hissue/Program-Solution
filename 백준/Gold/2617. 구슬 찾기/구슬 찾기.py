import sys
from collections import deque
N,M  = map(int,sys.stdin.readline().split())

bigger = [[] for _ in range(N+1)]
smaller = [[] for _ in range(N+1)]
mid = (N+1)//2
for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    bigger[a].append(b) 
    smaller[b].append(a)


def solution(arr,cnt,x):
    que = deque()
    que.append(x)
    visited[x] = True

    while que:
        ch = que.popleft()
        for i in arr[ch]:
            if not visited[i]:
                cnt+=1
                cnt= solution(arr,cnt,i)
    return cnt

answer = 0

for i in range(1,N+1):
    visited = [False]*(N+1)
    if not visited[i]:
        if solution(bigger,0,i) >= mid:
            answer+=1

        if solution(smaller,0,i) >= mid:
            answer+=1

print(answer)