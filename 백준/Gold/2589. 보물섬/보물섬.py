import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())
island = []
for _ in range(N):
    island.append(list(sys.stdin.readline().rstrip()))

visited = []

for i in range(N):
    for j in range(M):
        if island[i][j] == 'L':
            visited.append((i,j))

def bfs(x,y):
    global N,M
    que = deque()
    que.append((x,y))
    timetable = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[x][y] = True

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    result = -1
    
    while que:
        x,y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0 <=ny<M and island[nx][ny] == 'L':
                if not visited[nx][ny]:
                    timetable[nx][ny] = timetable[x][y] +1
                    visited[nx][ny] = True
                    que.append((nx,ny))
                    result = max(result,timetable[nx][ny])

    return result 


max_value = -1

for x,y in visited:
    max_value = max(max_value,bfs(x,y))

print(max_value)