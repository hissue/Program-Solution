# 크루스칼
import sys

# 입력
V,E = map(int,sys.stdin.readline().split())
tree = []
for _ in range(E):
    a,b,w = map(int,sys.stdin.readline().split())
    tree.append((a,b,w))

# 가중치 기준으로 정렬
tree.sort(key=lambda x : x[2])

# 노드의 루트 정보
pRoot = [ _ for _ in range(V+1)]

# 가중치의 합
result = 0

def find(x):
    if x != pRoot[x]:
        pRoot[x] = find(pRoot[x]) # 부모 루트 찾기
    return pRoot[x] # 본인의 부모 루트값 출력

def union(a,b,w):
    global result
    aRoot = find(a)
    bRoot = find(b)

    if aRoot != bRoot:
        if aRoot > bRoot:
            pRoot[aRoot] = bRoot
        else:
            pRoot[bRoot] = aRoot

        result+=w

for a,b,w in tree:
    union(a,b,w)

print(result)
