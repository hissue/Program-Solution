import sys

N = int(sys.stdin.readline())
result = 0
if N < 100:
    print(N)
else:
    for _ in range(100,N+1):
        temp = list(str(_))
        if (int(temp[0]) - int(temp[1]) == int(temp[1]) - int(temp[2])):
            result+=1
    print(99+result)