A = int(input())
B = input()
result = []

for b in B:
    result.append(A*int(b))        

for i in range(1,4):
    print(result[-i])
    result[-i]*=10**(i-1)
    
print(sum(result))