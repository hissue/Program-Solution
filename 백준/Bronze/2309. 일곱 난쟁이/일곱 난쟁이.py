import sys, itertools

arr = [int(sys.stdin.readline()) for _ in range(9)]
result = list(itertools.combinations(arr,7))
for _ in result:
    if sum(_) == 100:
        for data in sorted(_):
            print(data)
        break