import sys
n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
s=[]
arr.sort()
def dfs():
    if len(s) == m:
        print(*s)
        return
    
    for i in range(len(arr)):
        s.append(arr[i])
        dfs()
        s.pop()

dfs()