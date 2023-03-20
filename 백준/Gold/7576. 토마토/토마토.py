import sys
from collections import deque

#  M : 열, N : 행
M,N = map(int,sys.stdin.readline().split())
# 토마토 입력 받기
box = []

for i in range(N):
    box.append(sys.stdin.readline().rstrip().split())

# 상자 안에 토마토가 없는 경우
noTomato = 0

# 토마토가 전체 익었을 때 걸리는 기간
result = 0

# 남은 토마토의 개수
restTomato = 0

# 토마토의 익은 날짜
day = [[0 for _ in range(M)] for _ in range(N)]

# 익은 토마토의 인덱스
que = deque()

# 익은 토마토의 인덱스 및 모든 토마토가 익어있는 상태인지 판별
for i in range(N):
    for j in range(M):
        if box[i][j] == '1': # 현재 안익은 토마토 인덱스
            que.append((i,j))
        if box[i][j] != '0': # noTomato의 개수가  N*M의 개수와 동일하면 초기에 모든 토마토가 익어있는 상태
            noTomato +=1
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 시작
while que:
    x,y = que.popleft()
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<N and 0<=ny<M and box[nx][ny] == '0':
            box[nx][ny] = '1'
            day[nx][ny] = day[x][y] +1
            que.append((nx,ny))

            result = max(result,day[nx][ny])

# 모든 시간이 지나고 토마토 내 0이 있는지 확인
for i in range(N):
    restTomato += box[i].count('0')

if noTomato == N*M:
    print(0)
elif restTomato > 0:
    print(-1)
else:
    print(result)