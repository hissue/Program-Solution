import sys
sys.setrecursionlimit(10**7)
N,M = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    s,e = map(int,sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

cnt = 0
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