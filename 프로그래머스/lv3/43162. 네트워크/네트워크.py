def dfs(i,computers,visited):
    visited[i] = True
    stack = [computers[i]]
    while stack:
        x = stack.pop()
        for i in range(len(x)):
            if not visited[i] and x[i] == 1:
                visited[i] = True
                stack.append(computers[i])
    return visited  
def solution(n, computers):
    visited = [False for _ in range(n)]
    answer = 0
   
    for i in range(n):
        if not visited[i]:
            visited = dfs(i,computers,visited)
            answer+=1
    return answer