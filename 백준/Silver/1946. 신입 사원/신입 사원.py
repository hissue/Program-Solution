import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    sales = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    sales.sort()
    b_score = sales[0][1]
    cnt = 1
    for i in range(1,N):
        if sales[i][1] < b_score:
            cnt+=1
            b_score = sales[i][1]
    print(cnt)