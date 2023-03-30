import sys
sys.setrecursionlimit(10 ** 6)
N = int(sys.stdin.readline())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

# 상하좌우 
dx = [-1,1,0,0]
dy = [0,0,-1,1]

dp = [[0] *N for _ in range(N)]

def dfs(col,row):

    if dp[col][row]:
        return dp[col][row]
    
    # 방문 처리
    dp[col][row] = 1

    for i in range(4):
        nx = col + dx[i]
        ny = row + dy[i]

        # 범위 안에 있으며 현재 위치보다 대나무가 많다면
        if 0<=nx<N and 0<=ny<N and arr[col][row] < arr[nx][ny]:
            dp[col][row] = max(dp[col][row] , dfs(nx,ny)+1)

    return dp[col][row]

# 최대 횟수
result = 0
# dfs 끊어진 경우 더 이상 탐색이 불가능하므로 모든 칸 확인하기 위해서
for i in range(N):
    for j in range(N):
        # 미리 방문한 곳이면 pass
        if not dp[i][j]:
            result = max(result,dfs(i,j))

print(result)