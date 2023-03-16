import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0

for i in range(M):
    s,e = map(int,sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(v):
    global cnt
    visited[v] = True
    for q in graph[v]:
        if visited[q] == False:
            visited[q] = True
            cnt+=1
            dfs(q)
    
dfs(1)
print(cnt)