import sys

N = sys.stdin.readline()
if N[:2] == '0x':
    print(int(N[2:],16))

elif N[:1] == '0' :
    print(int(N[1:],8))

else:
    print(N)