import sys
from itertools import combinations
N = int(sys.stdin.readline())
S = list(map(int,sys.stdin.readline().split()))

data = {}
max_data = sum(S)+1

for i in range(1,max_data+1):
    if i not in data:
        data[i] = 0

for i in range(1,N+1):
    for result in combinations(S,i):
        temp = sum(result)
        if data[temp] == 0:
            data[temp] = temp

for i in data.keys():
    if data[i] == 0:
        print(i)
        break