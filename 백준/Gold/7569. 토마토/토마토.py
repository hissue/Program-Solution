import sys
from collections import deque
# M이 y N이 x H가 z
M,N,H = map(int,sys.stdin.readline().split())
tomatos = [[] for _ in range(H) ] # 3차원 배열

for i in range(H): # 위 아래 
    for j in range(N):# 세로
        tomatos[i].append(list(map(int,sys.stdin.readline().split()))) # 가로

# 상 하 좌 우 앞 뒤
dz = [-1,1,0,0,0,0]
dx = [0,0,-1,1,0,0]
dy = [0,0,0,0,-1,1]

que = deque()

# 초기 안익은 토마토 개수 
temp = 0 
# 초기에 익어있는 토마토 찾기
for z in range(H): # 상하
    for i in range(N): # 앞뒤
        for j in range(M): #좌우
            if tomatos[z][i][j] == 1:
                que.append((0,z,i,j)) 
            elif tomatos[z][i][j] == 0: #안익은 토마토 개수
                temp+=1

while que:
    c,z,x,y = que.popleft()
    
    for i in range(6):
        nz = z + dz[i] # z축이 움직임(상하)
        nx = x + dx[i] # x축이 움직임(앞뒤)
        ny = y + dy[i] # y축이 움직임(좌우)

        if 0<=nz<H and 0<=nx<N and 0<=ny<M and tomatos[nz][nx][ny] == 0:
            tomatos[nz][nx][ny] = 1
            que.append((c+1,nz,nx,ny))
        
    result = c

# 남은 안익은 토마토 개수
rest = 0
for z in range(H): # 상하
    for i in range(N): # 앞뒤
        for j in range(M): #좌우
            if tomatos[z][i][j] == 0: #남은 안익은 토마토 개수
                rest+=1

if temp==0: #초기부터 안익은 토마토가 없으면
    print(0)
elif rest > 0: # 안익은 토마토가 한 개라도 있으면
    print(-1)
else:
    print(result) # 토마토 익는데 걸린 날짜