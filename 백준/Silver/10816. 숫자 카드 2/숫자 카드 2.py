import sys

N = int(sys.stdin.readline())
NS = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
MM = list(map(int,sys.stdin.readline().split()))

MS = sorted(MM)
result = {}

for i in MS:
    result[i]=0

for target in NS:
    start = 0
    end = len(MS)-1
    while start<=end:
        mid = (start+end)//2
        if MS[mid] == target:
            result[target]+=1 
            break
        
        elif MS[mid] < target:
            start = mid+1
        else:
            end = mid-1

for i in MM:
    print(result[i],end=" ")