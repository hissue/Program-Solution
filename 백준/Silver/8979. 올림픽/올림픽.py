import sys

N,K = map(int,sys.stdin.readline().split())

olympic = []

for _ in range(N):
    arr = list(map(int,sys.stdin.readline().split()))
    olympic.append(arr)

    olympic.sort(key=lambda x: (-x[1],-x[2],-x[3]))

cnt=1

for i in range(1,len(olympic)):
    if i==K:
        break
    
    if str(olympic[i-1][1:]) == str(olympic[i][1:]):
        cnt = i
    else:
        cnt+=1

print(cnt)
