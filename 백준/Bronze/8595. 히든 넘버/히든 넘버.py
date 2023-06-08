import sys
N = int(sys.stdin.readline())
data = sys.stdin.readline().rstrip()
temp =''
answer = 0
for d in data:
    if d.isdigit():
        temp+=d
    elif d.isalpha() and temp:
        answer+=int(temp)
        temp=''
if temp:
    print(answer+int(temp))
else:
    print(answer)