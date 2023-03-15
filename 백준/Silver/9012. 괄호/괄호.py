import sys

N = int(sys.stdin.readline())
for _ in range(N):
    arrs = sys.stdin.readline().rstrip()
    stack = []
    for arr in arrs:
        if stack and stack[-1] == '(' and arr == ')':
            stack.pop()
        else:
            stack.append(arr)
            
    if len(stack)==0:
        print('YES')
    else:
        print('NO')
        

