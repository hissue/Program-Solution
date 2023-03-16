import sys
def dfs(graph, start_node):
    visit = list()
    stack = list()
    stack.append(start_node)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(sorted(graph[node],reverse=True))
    return visit

def bfs(graph, start_node):
    visit = list()
    queue = list()
    queue.append(start_node)
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    return visit
    
N,M,V = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    k,v = map(int,sys.stdin.readline().split())
    graph[k].append(v)
    graph[v].append(k)

for i in range(len(graph)):
    graph[i] = sorted(graph[i])
print(*dfs(graph,V))
print(*bfs(graph,V))