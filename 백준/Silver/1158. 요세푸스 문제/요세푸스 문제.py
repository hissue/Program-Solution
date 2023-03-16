N,k = map(int,input().split())
arr = [i for i in range(1,N+1)]
result = []
results=''
idx = 0
while len(arr) > 0:
    idx = (idx +(k-1))%len(arr)
    result.append(arr.pop(idx))

for i in result:
    results+=(str(i)+', ')


print("<"+results[:-2]+">")