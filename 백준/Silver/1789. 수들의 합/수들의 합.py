import sys

temp = int(sys.stdin.readline())
num = 1
sum = 0
cnt = 0
while True:
    sum+=num
    cnt+=1
    num+=1
    if sum > temp:
        cnt-=1
        break

print(cnt)