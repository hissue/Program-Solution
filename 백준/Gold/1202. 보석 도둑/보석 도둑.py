import sys,heapq

# 보석 개수, 가방 개수
N,K = map(int,sys.stdin.readline().split())

# 무게, 가격
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
arr.sort()

# 가방 무게
bags = [int(sys.stdin.readline()) for _ in range(K)]
bags.sort()

# 최대 합
temp = []
result = 0

# m : 무게, w : 가격
for bag in bags:
    while arr and arr[0][0] <= bag:
        heapq.heappush(temp,-arr[0][1])
        heapq.heappop(arr)
    
    if temp:
        result+=heapq.heappop(temp)


print(-result)