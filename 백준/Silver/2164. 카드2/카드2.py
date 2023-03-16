import sys
from collections import deque

N = int(sys.stdin.readline())
words = deque( i for i in range(1,N+1))

while len(words)!=1:
    words.popleft()
    words.append(words.popleft())
print(*words)