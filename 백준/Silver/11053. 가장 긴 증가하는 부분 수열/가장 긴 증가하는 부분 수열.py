N = int(input())

s = [0]*N
s[0] = 1

dp = list(map(int,input().split()))

for i in range(1,N):
    for j in range(i):
        if dp[i] > dp[j] :
            s[i] = max(s[j],s[i])
    s[i]+=1
    
print(max(s))