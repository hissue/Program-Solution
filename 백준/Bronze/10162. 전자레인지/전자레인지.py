import sys

timer = [300,60,10]

T = int(sys.stdin.readline())

result = [0,0,0]

for i in range(len(timer)):
    temp = 0
    if T//timer[i] > 0:
        temp = T//timer[i]
        T = T%timer[i]

    result[i]+=temp

if T !=0:
    print(-1)
else:
    print(*result)