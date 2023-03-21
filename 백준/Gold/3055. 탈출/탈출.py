import sys
from collections import deque

R,C = map(int,sys.stdin.readline().split())

# 티떱숲
forest = []
for _ in range(R):
    forest.append(list(sys.stdin.readline().rstrip()))


# 시작
def bfs():

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    que = deque()
    # 초기 고슴도치 및 비버 위치  
    for i in range(R):
        for j in range(C):
            # 고슴도치의 위치
            if forest[i][j] == 'S':
                que.append((0,i,j))
            # 비버의 위치
            elif forest[i][j] == 'D':
                x_bibber, y_bibber = i,j
    
    # 초기 홍수 위치
    for i in range(R):
        for j in range(C):
            if forest[i][j] == '*':
                que.append((0,i,j))
    
    # 걸린 날짜
    day = 0

    # 이동 시작
    while que:
        day,x,y = que.popleft()

        # 고슴이와 홍수가 이동할 수 있는 상하좌우
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            
            if 0<=nx<R and 0<=ny<C:
                # 고슴이의 이동
                if forest[x][y] == 'S' and (forest[nx][ny] == '.' or forest[nx][ny] == 'D'):
                    forest[nx][ny] = 'S'
                    que.append((day+1,nx,ny))
                
                    # 비버굴 위치에 고슴이가 있으면 return
                    if forest[x_bibber][y_bibber] == 'S': 
                        return day+1
            
                # 홍수 이동
                if forest[x][y] == '*' and (forest[nx][ny] == '.' or forest[nx][ny] == 'S'):
                    forest[nx][ny] = '*'
                    que.append((day+1,nx,ny))

    # 비버굴 위치에 고슴이가 없으면 return
    return 'KAKTUS'

print(bfs())