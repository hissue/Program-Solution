import sys

N = int(sys.stdin.readline())
arr = [sys.stdin.readline().rstrip() for _ in range(N)]
result = []
def recursive(x,y,N):
    color = arr[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if color!=arr[i][j]:
                result.append('(')
                recursive(x,y,N//2)
                recursive(x,y+N//2,N//2)
                recursive(x+N//2,y,N//2)
                recursive(x+N//2,y+N//2,N//2)
                result.append(')')
                return
    if color =='1':
        result.append('1')
    else:
        result.append('0')

recursive(0,0,N)
print(''.join(result))