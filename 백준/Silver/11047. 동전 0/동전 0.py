import sys

N, K = map(int,sys.stdin.readline().split())

arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort(reverse=True)
cnt = 0
for coin in arr:
    if K >= coin:
        cnt+=K//coin
        K%=coin
    
    if K == 0:
        break
    
print(cnt)