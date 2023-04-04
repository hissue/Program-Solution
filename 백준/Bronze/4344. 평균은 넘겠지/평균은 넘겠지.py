T = int(input())
for _ in range(T):
    arr = list(map(int,input().split()))
    avg = sum(arr[1:])/arr[0]
    result = []
    for i in arr[1:]:
        if i > avg:
            result.append(i)
    
    print("{:.3f}%".format(round(len(result))/arr[0]*100))