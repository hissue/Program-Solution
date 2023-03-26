import sys
N = int(sys.stdin.readline())
cur = 1
while N>0:
    if N//3 > 0:
        N -=3
    else:
        N-=1
    cur = -cur
    
if cur == -1:
    print('SK')
else:
    print('CY')
