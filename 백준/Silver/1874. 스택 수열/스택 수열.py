import sys

N = int(sys.stdin.readline())
arrs = [int(sys.stdin.readline()) for _ in range(N)]
stack = []
result = []
cnt = 0
for data in range(1,N+1):
    stack.append(data)
    result.append('+')
    
    while stack and stack[-1] == arrs[cnt]:
        stack.pop()
        result.append('-')
        cnt+=1
    
if stack:
    print('NO')
else:
    for i in result:
        print(i)
