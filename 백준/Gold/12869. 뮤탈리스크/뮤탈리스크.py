from itertools import permutations
def dfs(x,y,z,cnt):
    global ans
    if x <=0 and y <=0 and z<=0:
        if ans > cnt:
            ans = cnt
            return

    x=0 if x <=0 else x
    y=0 if y <=0 else y
    z=0 if z <=0 else z

    if dp[x][y][z] <= cnt and dp[x][y][z] != 0:
        return
    
    dp[x][y][z] = cnt

    for a,b,c in permutations([9,3,1],3):
        dfs(x - a, y - b, z - c, cnt + 1)


N = int(input())
arr = list(map(int,input().split()))
while len(arr) < 3:
    arr += [0]
ans = 61
dp = [[[61] * (61) for _ in range(61)] for _ in range(61)]
dfs(arr[0],arr[1],arr[2],0)
print(ans)