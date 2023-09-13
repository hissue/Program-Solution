import sys
N,M = map(int,sys.stdin.readline().split())
s = []
def dfs()-> None :
    if len(s) == M:
      print(*s)
      return

    for i in range(1,N+1):
       if i not in s:
          s.append(i)
          dfs()
          s.pop()

dfs()