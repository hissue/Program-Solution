import sys
from collections import deque

# 보드의 크기
N = int(sys.stdin.readline())
board = [[0] * (N) for _ in range(N)]

# 정사각 보드 제작 및 사과 위치 입력
K = int(sys.stdin.readline())
for i in range(K):
    xap,yap = map(int,sys.stdin.readline().split())
    board[xap-1][yap-1] = 1

# 뱀의 방향 변환 횟수 (시간,방향 전환)
L = int(sys.stdin.readline())
direction = [sys.stdin.readline().split() for _ in range(L)]

# 0 : 우, 1: 하, 2: 좌, 3: 상 이동
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 시작 오른쪽으로 이동
d = 0 

# 시간
time = 0

# 시작 위치 0,0 선언 (=1,1에서 시작)
que = deque()
que.append((0,0))

# 시작
while que:
    x,y = que[-1]
    time+=1

    # 뱀 이동 좌표
    nx = x + dx[d]
    ny = y + dy[d]
    
    # 뱀이 보드 내에 있을 때,
    if 0<=nx<N and 0<=ny<N:
        # 현재 위치에 사과가 있다면
        if board[nx][ny] == 1:
            board[nx][ny] = 2
        # 자신과 부딪히거나 
        elif (nx,ny) in que:
            break
        # 현재 위치에 사과가 없다면
        else:
            que.popleft()
        board[nx][ny] = 3
    # 뱀이 보드 내에 없으면 break
    else: break

    que.append((nx,ny))

    # 방향 전환
    for i in direction:
        if int(i[0]) == time:
            # 오른쪽으로 90도 회전
            if i[1] =='D':
                d = (d+1)%4
            # 왼쪽으로 90도 회전 (만약 d가 0일때, 왼쪽으로 회전하면 d 가 3이 되어 위로 이동(파이썬 특징))
            else: 
                d = (d-1)%4
            break

print(time)