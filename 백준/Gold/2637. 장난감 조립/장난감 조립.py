import sys
from collections import deque

N = int(sys.stdin.readline()) # 완제품 번호
M = int(sys.stdin.readline()) # 부품 관계 개수
perfect = [[] for _ in range(N+1)] # 연결된 간선 정보
table = [0] * (N+1) # 차수의 개수
result = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M): # 정보 입력 받기
    X,Y,Z = map(int,sys.stdin.readline().split())
    perfect[Y].append((X,Z))
    table[X] +=1 # 차수 개수 넣어주기

que = deque()

for i in range(1,N+1): # 차수가 0인 노드 넣어주기
    if table[i] == 0:
        que.append(i) 

while que:
    now = que.popleft() # 차수가 0인 정점 중 하나를 빼고
    for next,next_need in perfect[now]: # 해당 정점과 연결되어 있는 점을 모두 출력하여
        if result[now].count(0) != N + 1:#중간 부품이라면
           for i in range(1,N+1):
                result[next][i] += result[now][i] * next_need
        else: # 기본 부품에 포함된다면
            result[next][now] += next_need
        table[next]-=1 # 간선을 없애고
        if table[next] == 0: # 정점의 차수가 0이라면 추가
            que.append(next)

for i in range(1,N+1):
    if result[N][i] > 0:
        print(i,result[N][i])