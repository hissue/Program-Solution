import sys
sys.setrecursionlimit(10**7)

computers = int(sys.stdin.readline())
pairs = int(sys.stdin.readline())

network = [[] for _ in range(computers+1)]
visited = []
cnt = 0

for i in range(pairs):
    s,e = map(int,sys.stdin.readline().split())
    network[s].append(e)
    network[e].append(s)

def dfs(v):
    global cnt
    visited.append(v)
    for i in network[v]:
        if i not in visited:
            visited.append(i)
            cnt+=1
            dfs(i)

dfs(1)
print(cnt)