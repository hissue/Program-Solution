import sys
import heapq
N,K = map(int,sys.stdin.readline().split())

arr = []

for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))

S,X,Y = map(int,sys.stdin.readline().split())

birus = []
visited = [[0]*(N) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            heapq.heappush(birus,(0,arr[i][j],i,j))
            visited[i][j] = arr[i][j]

while birus:
    time,num, x,y = heapq.heappop(birus)

    if time == S:
        break

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
            visited[nx][ny] = num
            heapq.heappush(birus,(time+1,num,nx,ny))
            
print(visited[X-1][Y-1])