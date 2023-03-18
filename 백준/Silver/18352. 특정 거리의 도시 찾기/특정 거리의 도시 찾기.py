import sys
from collections import deque
sys.setrecursionlimit(10**6)
N, M, K, X = map(int,sys.stdin.readline().split())
citys = [[] for _ in range(N+1)]
visited = [N] * (N+1)
visited[X] = 0
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    citys[a].append(b)

def bfs(x):
    deq = deque()
    deq.append(x)

    while deq:
        root = deq.popleft()
        for i in citys[root]:
            if visited[i] ==N:
                visited[i] = min(visited[i],visited[root]+1)
                deq.append(i)

bfs(X)

if K not in visited:
    print(-1)
else:
    for i in range(len(visited)):
        if visited[i] == K:
            print(i)