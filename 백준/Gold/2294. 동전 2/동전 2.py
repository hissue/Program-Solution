n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# 최소 동전 개수를 저장하기 위한 리스트를 INF로 초기화합니다.
INF = 10001
dp = [INF]*(k+1)
dp[0] = 0

for coin in coins:
    for j in range(coin, k+1):
        dp[j] = min(dp[j], dp[j-coin]+1)

# dp[k]가 INF라면, k원을 만드는 것이 불가능하다는 뜻이므로 -1을 출력합니다.
if dp[k] == INF:
    print(-1)
else:
    print(dp[k])