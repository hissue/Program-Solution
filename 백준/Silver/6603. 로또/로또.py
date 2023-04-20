import sys
from itertools import combinations
while(1):
    lotto = list(map(int,sys.stdin.readline().split()))
    
    if lotto[0] == 0:
        break
    
    for result in combinations(lotto[1:],6):
        print(*result)

    print()