import sys

N = int(sys.stdin.readline())
A =[0] + list(map(int,sys.stdin.readline().rstrip()))
cnt = 0
road = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for i in range(N-1):
    a,b = map(int,sys.stdin.readline().split())
    road[a].append(b)
    road[b].append(a)

def dfs(start): 
    global cnt

    for i in road[start]:
        if not visited[i]: 
            if A[i] == 1:
                cnt+=1
            else:
                visited[i] = True  
                dfs(i)
                visited[i] = False
            
for i in range(1,N+1):
    if A[i] != 0:
        visited[i] = True
        dfs(i)
        visited[i] = False

print(cnt)