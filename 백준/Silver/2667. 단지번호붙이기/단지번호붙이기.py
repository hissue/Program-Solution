import sys
N = int(sys.stdin.readline())
maps = []
for _ in range(N):
    maps.append(list(sys.stdin.readline().rstrip()))

visited = [[False] * N for _ in range(N)]

def dfs(i,j):
    stack =[]
    stack.append((i,j))
    v_cnt=1

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while stack:
        x,y = stack.pop()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and maps[nx][ny] != '0' and visited[nx][ny] == False:
                visited[nx][ny] = True
                v_cnt +=1
                stack.append((nx,ny))
    return v_cnt

cnt = 0
result = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and maps[i][j] != '0':
            visited[i][j] = True
            result.append(dfs(i,j))
            cnt+=1
print(cnt)
for _ in sorted(result):
    print(_)