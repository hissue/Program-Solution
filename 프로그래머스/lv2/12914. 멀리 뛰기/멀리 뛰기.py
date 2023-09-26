def solution(n):
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    for idx in range(2,n+1):
        dp[idx] = dp[idx-2] + dp[idx-1]

    return dp[n]%1234567