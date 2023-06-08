import sys
N,M = input().split()
A = list(map(int,sys.stdin.readline().split(' ')))
B = list(map(int,sys.stdin.readline().split(' ')))
result = A+B
result.sort()
print(*result)