C = int(input())
nums = []
dps = [0]*12
dps[1]=1
dps[2]=2
dps[3]=4
for i in range(C):
    N = int(input())
    for i in range(4,N+1):
        dps[i] = dps[i-1]+dps[i-2]+dps[i-3]
    nums.append(N)
for num in nums:
    print(dps[num])