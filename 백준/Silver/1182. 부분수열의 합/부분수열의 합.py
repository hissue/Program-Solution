import sys
from itertools import combinations
N,S = map(int,sys.stdin.readline().split())

per = list(map(int,sys.stdin.readline().split()))

answer=0

for i in range(1,N+1):
    for pers in combinations(per,i):
        if sum(pers) == S:
            answer+=1

print(answer)