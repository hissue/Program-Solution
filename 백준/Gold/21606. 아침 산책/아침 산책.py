import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
A =[0] + list(map(int,sys.stdin.readline().rstrip()))
cnt = 0
road = [[] for _ in range(N+1)]
check_visited = [False] * (N+1)

for i in range(N-1):
    a,b = map(int,sys.stdin.readline().split())
    road[a].append(b)
    road[b].append(a)

def dfs(start): 
    global cnt
    for i in road[start]:
        if not check_visited[i]: 
            if A[i] == 1:
                cnt+=1
            else:
                check_visited[i] = True  
                dfs(i)
    check_visited[start] = True
            
for i in range(1,N+1):
    if A[i] != 0:
        check_visited[i] = True
        dfs(i)

print(cnt)