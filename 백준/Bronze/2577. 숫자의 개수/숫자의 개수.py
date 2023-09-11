data1 = int(input())
data2 = int(input())
data3 = int(input())

dicts = {}
result = data1*data2*data3
for _ in range(10):
    dicts[_] = 0

while(result>0):
    rest=result%10
    result//=10
    dicts[rest] += 1

for _ in range(10):
    print(dicts[_])
    