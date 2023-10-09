import sys
n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
s = []
def dfs(start):
    if len(s) == m:
        print(*s)
        return
    
    for i in range(start, len(arr)):
        s.append(arr[i])
        dfs(i)
        s.pop()
    
dfs(0)