import sys

N = int(sys.stdin.readline())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp = [[-1]*(N) for _ in range(N)]

def dfs(col,row,jump):
    if col == N-1 and row == N-1:
        return 1

    if dp[col][row] !=-1:
        return dp[col][row]
    
    dp[col][row] = 0
    
    dx = [jump,0]
    dy = [0,jump]

    for i in range(2):
        nx = col + dx[i]
        ny = row + dy[i]

        if 0<=nx<N and 0<=ny<N:
            dp[col][row] += dfs(nx,ny,arr[nx][ny])

    return dp[col][row] 

print(dfs(0,0,arr[0][0]))