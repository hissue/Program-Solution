import sys

M,N = map(int,sys.stdin.readline().split())

m = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]

visited = [[-1]*N for _ in range(M)]

def dfs(col, row):
    
    if col == M-1 and row == N-1:
        visited[col][row] = 1
        return visited[col][row]
    
    if visited[col][row] !=-1:
        return visited[col][row]
    
    visited[col][row] = 0

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    for i in range(4):
        nx = col + dx[i]
        ny = row + dy[i]

        if 0<=nx<M and 0<=ny<N and m[col][row] > m[nx][ny]:
            visited[col][row] += dfs(nx,ny)

    return visited[col][row]

print(dfs(0,0))