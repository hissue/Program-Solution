import sys
sys.setrecursionlimit(10**6)
N,M = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(i):
    
    for node in graph[i]:
        if not visited[node]:
            visited[node] = True
            dfs(node)

for i in range(1,N+1):
    if not visited[i]:
        visited[i] = True
        cnt+=1
        dfs(i)

print(cnt)