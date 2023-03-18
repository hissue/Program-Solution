import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())
height = [[] for _ in range(N+1)]
table = [0] * (N+1)

for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    height[a].append(b)
    table[b] +=1

que = deque()

for i in range(1,N+1):
    if table[i] == 0:
        que.append(i)

while que:
    node = que.popleft()
    print(node)
    for i in height[node]:
        table[i]-=1
        if table[i] == 0:
            que.append(i)
