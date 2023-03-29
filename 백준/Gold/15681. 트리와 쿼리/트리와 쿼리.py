import sys
sys.setrecursionlimit(10 ** 6)
# N : 루트 정점의 수, R : 루트의 번호, Q : 쿼리의 수
N,R,Q = map(int,sys.stdin.readline().split())
# 정점의 값
tree = {}
# DP 저장
dp = [0 for _ in range(N+1)]
for _ in range(N-1):
    node1, node2 = map(int,sys.stdin.readline().split())
    if node1 not in tree:
        tree[node1] = []
    if node2 not in tree:
        tree[node2] = []
    tree[node1].append(node2)
    tree[node2].append(node1)
# 쿼리의 수
q=[int(sys.stdin.readline()) for _ in range(Q)]

# dfs 재귀문
def dfs(root):
    # root에 방문했었다면 더 이상 재귀 x
    if dp[root]:
        return dp[root]
    # 방문처리
    dp[root] = 1
    # 정점에 연결된 루트 확인
    for node in tree[root]:
        # 방문하지 않았다면
        if not dp[node]:
            # 깊이 탐색 진행
            dp[root] += dfs(node)
    return dp[root]

# 시작
dfs(R)
                
# 해당 쿼리 값 출력
for i in q:
    print(dp[i])