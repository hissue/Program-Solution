import sys,heapq

N = int(sys.stdin.readline())

room = []
for _ in range(N):
    room.append(list(map(int,sys.stdin.readline().rstrip())))

distance=[[-1 for _ in range(N)] for _ in range(N)] 

# 방향
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 움직이는 위치
que = []
distance[0][0] = 0

heapq.heappush(que,(0,0,0))

while que:
    a,x,y = heapq.heappop(que)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<N and distance[nx][ny] == -1:
            if room[nx][ny] == 1:
                distance[nx][ny] = a
                heapq.heappush(que,(a,nx,ny))
            else:
                distance[nx][ny] = a+1
                heapq.heappush(que,(a+1,nx,ny))
        

print(distance[N-1][N-1])