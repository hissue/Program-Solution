import sys
from collections import deque
N,K = map(int,sys.stdin.readline().split())

arr = []

for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))

S,X,Y = map(int,sys.stdin.readline().split())

birus = deque()

temp = []

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            temp.append((arr[i][j],0,i,j))

temp.sort()

birus = deque(temp)

while birus:
    num,time,x,y = birus.popleft()

    if time == S:
        break

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<N and arr[nx][ny] == 0:
            arr[nx][ny] = num
            birus.append((num,time+1,nx,ny))

print(arr[X-1][Y-1])