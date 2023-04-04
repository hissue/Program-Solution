T = int(input())

for i in range(T):
    ox = input()
    temp = 0
    result = 0
    for j in ox:
        if 'X' == j:
            temp = 0
            continue
        else:
            temp+=1
        result+=temp
    print(result)