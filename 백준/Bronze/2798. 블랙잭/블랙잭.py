import sys, itertools
N, M = map(int,sys.stdin.readline().split(" "))
datas = list(map(int,sys.stdin.readline().split(" ")))
min_data = 100000
result = []
# M을 넘지 않으면서 M에 최대한 가까운 카드 3장
for _ in itertools.combinations(datas,3):
    tmp = sum(_)
    if tmp <= M and M-tmp <= min_data:
        min_data = M-tmp
        result = _
print(sum(result))
