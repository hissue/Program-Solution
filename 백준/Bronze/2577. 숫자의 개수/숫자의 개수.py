arr = list(int(input()) for _ in range(3))
temp = 1
result = [0]*10
for i in arr:
    temp*=i

for i in str(temp):
    result[int(i)]+=1

for i in range(10):
    print(result[i])