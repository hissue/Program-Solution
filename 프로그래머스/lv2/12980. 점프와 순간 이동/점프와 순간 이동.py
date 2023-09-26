def solution(n):
    # 시간 초과
    # dp = [0 for _ in range(n+1)]
    # dp[1] = 1
    # for idx in range(2, n+1):
    #     if idx%2:
    #         dp[idx] = dp[idx-1]+1
    #     else:
    #         dp[idx] = dp[idx//2]
    # return dp[n]
    # 효율성 해결
    answer=0
    while n>0:
        if n%2:
            answer+=1
            n = (n-1)//2
        else:
            n//=2
    return answer
    