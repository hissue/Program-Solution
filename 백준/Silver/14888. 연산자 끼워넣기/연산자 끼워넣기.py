import sys
from itertools import permutations

N = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
ops = list(map(int,sys.stdin.readline().split()))
temp = ['+','-','x','/']

result =''
for op in range(len(ops)):
    result+=(temp[op]*ops[op])
mi = sys.maxsize
mx = -sys.maxsize

for i in set(map(tuple,permutations(result,N-1))):
    sol = data[0]
    for j in range(N-1):
        if i[j] == '+':
            sol+=data[j+1]
        elif i[j] == '-':
            sol-=data[j+1]
        elif i[j] == 'x':
            sol*=data[j+1]
        else:
            if sol < 0 and data[j+1] > 0 :
                sol=-((abs(sol)) // data[j+1])
            else:
                sol//=data[j+1]

    if sol < mi:
        mi = sol
    
    if sol > mx:
        mx = sol

print(mx)
print(mi)