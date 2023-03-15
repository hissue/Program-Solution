import sys

N = int(sys.stdin.readline())
budgets = sorted(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())

start = 0
end = budgets[-1]
result = 0

while start<=end:
    mid = (start+end)//2
    total = 0
    for budget in budgets:
        if budget <= mid:
            total+=budget
        else:
            total+=mid
    if total > M:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)