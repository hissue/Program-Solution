import sys
n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
s = []
def dfs():
    if len(s) == m:
        print(*s)
        return

    for i in range(len(arr)):
        if arr[i] not in s:
            s.append(arr[i])
            dfs()
            s.pop()

dfs()