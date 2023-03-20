import sys
from collections import deque
N,M,K,X = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
result = []

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)

que = deque()
que.append(X)
visited[X] = 1
while que:
    node = que.popleft()
    for i in graph[node]:
        if visited[i] == 0:
            visited[i] = visited[node]+1
            que.append(i)

for i in range(len(visited)):
    if visited[i] == K+1:
        result.append(i)

if not result:
    print(-1)

else:
    for _ in result:
        print(_)