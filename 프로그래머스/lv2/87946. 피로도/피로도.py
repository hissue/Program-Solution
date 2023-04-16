answer = 0 
def dfs(cnt, current, visited, dungeons):
    global answer
    answer = max(answer,cnt)
    for i in range(len(dungeons)):
        if not visited[i] and current >= dungeons[i][0]:
            visited[i] = True
            dfs(cnt+1,current-dungeons[i][1], visited, dungeons)
            visited[i] = False

def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    dfs(0,k,visited,dungeons)
    return answer
