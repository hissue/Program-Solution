import sys

N,C = map(int,sys.stdin.readline().split())

wifi = list(int(sys.stdin.readline()) for _ in range(N))

wifi.sort()

start = 1
end = wifi[-1]

result = 0

while start <= end:
    first = wifi[0]
    mid = (start+end)//2
    cnt = 1
    for i in range(1,len(wifi)):
        if wifi[i] >= first+mid:
            first = wifi[i]
            cnt+=1

    if cnt < C:
        end = mid -1
    else:
        result = mid
        start = mid + 1

print(result)