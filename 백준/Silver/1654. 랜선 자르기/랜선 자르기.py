import sys

K, N = map(int,sys.stdin.readline().split())
lines = list(int(sys.stdin.readline()) for i in range(K))

result = 0 # 개수만큼 최대로 자를 수 있는 랜선 값
start = 1 # 최소 랜선 값
end = max(lines) # 최대 랜선 값

while start <= end:
    cnt = 0
    mid = (start+end)//2

    for line in lines:
        cnt+= (line//mid)

    if cnt >= N:
        result = mid
        start = mid+1

    else:
        end = mid-1

print(result)