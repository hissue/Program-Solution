import sys
N = int(sys.stdin.readline())
data = list(map(int,[sys.stdin.readline() for _ in range(N)]))
for _ in sorted(data):
    print(_)