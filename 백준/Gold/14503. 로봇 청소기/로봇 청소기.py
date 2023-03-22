import sys
from collections import deque

# N : 행, M : 열
N,M = map(int,sys.stdin.readline().split())

# d - 0:상, 3:좌, 2:하, 1:우
x,y,d = map(int,sys.stdin.readline().split())

# 좌표 - 0: 안치운 칸, 1: 벽
rooms = []
for _ in range(N):
    rooms.append(list(sys.stdin.readline().rstrip().split()))

visited = [['0'] * M for _ in range(N)]

# 0 -> 3 -> 2 -> 1
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 청소한 방의 갯수
cnt=1
visited[x][y] = '1'

# 시작
while True:
    flag = 0
    # 반시계 방향으로 회전
    for _ in range(4):
        nx = x + dx[(d-1)%4]
        ny = y + dy[(d-1)%4]
        
        # 현재 방향 
        d = (d-1)%4

        if 0<=nx<N and 0<=ny<M and rooms[nx][ny] == '0':
            if visited[nx][ny] == '0':
                visited[nx][ny] = '1'
                cnt+=1
                x = nx
                y = ny
                flag = 1 
                break

    # 청소 안 된 칸 하나도 x
    if flag == 0:
        # 후진 했을 때, 벽이라면
        if rooms[x-dx[d]][y-dy[d]] == '1':
            print(cnt)
            break
           
       
        else:
            x,y = x-dx[d],y-dy[d]