# 구현 실패
# 수빈이는 N, 동생 K
# 수빈이는 걷거나 순간이동 - 걸을 때 : X-1 OR X+1(1초 후) , 순간이동 : 2*X (1초 후)
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간

import sys
from collections import deque
N,K = map(int,sys.stdin.readline().split())
visited = [[] for _ in range(100001)]

def bfs(x):
    global result
    que = deque()
    que.append((x,0))

    while que:
        cur,time = que.popleft()
        
        if 0<=cur<100001:
            if cur == K:
                result = time
                break

            if not visited[cur]:
                visited[cur] = True
                que.append((cur - 1,time+1))
                que.append((cur + 1,time+1))
                que.append((cur * 2,time+1))
            
result = 0

bfs(N)
print(result)