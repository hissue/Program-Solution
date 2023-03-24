import sys
# N : 주어지는 물품의 수, K : 최대 버틸 수 있는 무게
N,K = map(int,sys.stdin.readline().split())

bag = [[0,0]]
dp = [[0 for _ in range(K+1)] for _ in range(N+1)] 

for _ in range(N):
    # W : 물건의 무게, V : 물건의 가치 
    W,V = map(int,sys.stdin.readline().split())
    bag.append([W,V])


for i in range(1,N+1):
    for j in range(1,K+1):
        w_cur = bag[i][0]
        v_cur = bag[i][1]
        
        if j < w_cur:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v_cur+dp[i-1][j-w_cur],dp[i-1][j])


print(dp[N][K]) # K 무게의 최대 가치 값