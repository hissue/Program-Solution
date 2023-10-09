import sys
L,C = map(int,sys.stdin.readline().split())
arr = list(sys.stdin.readline().split())
result = []
moems = ['a','e','i','o','u']
def dfs(next,cnt,visited):
    if cnt == L:
        temp=0
        for i in visited:
            if i in moems:
                temp+=1
        if temp >= 1 and L-temp >=2:
            result.append(''.join(sorted(visited)))
            return
    
    for i in range(next,C):
        visited.append(arr[i])
        dfs(i+1,cnt+1,visited)
        visited.pop()     
dfs(0,0,[])
# print(result)
print(*sorted(result))