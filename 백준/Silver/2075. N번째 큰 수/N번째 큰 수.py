import sys,heapq

N = int(sys.stdin.readline())
result = []
for i in range(N):
    result.extend(map(int,sys.stdin.readline().split()))
    if len(result) > N:
        result.sort(reverse=True)
        result = result[:N]
print(result[-1])