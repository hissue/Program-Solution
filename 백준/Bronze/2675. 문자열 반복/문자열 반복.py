T = int(input())

for _ in range(T):
    arr = input()
    for i in arr[2:]:
        print(i*int(arr[0]),end='')
    print()