# 전기용품 사용순서를 알아내 플러그를 빼는 횟수를 최소화
# 1. 가장 늦게 나오는 경우 2. 뒤에 안나오는 경우
 
import sys
from collections import deque
N,K = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

# 멀티탭의 위치 인덱스
mt = {}

# 플러그 꽂혀 있는 전자기기
plug = []

# 총 뽑는 횟수
cnt = 0

# 사전에 for문을 통해 인덱스 위치 저장
for i in range(K):
    if arr[i] not in mt:
        mt[arr[i]] = []
    mt[arr[i]].append(i)

# 뒤에 안나오는 경우 확인
for p in arr:
    if p in plug:
        if mt[p]:
            mt[p].pop(0)
    # 플러그 내에 없는 경우
    else:
        # 꽂혀있는 플러그 갯수가 N 개 이하인 경우
        if len(plug) < N:
            plug.append(p)
            mt[p].pop(0)
            continue

        temp = 0
        idx = 0
        # 플러그의 인덱스 확인 
        for i in plug:
            # 인덱스가 더 이상 안나오는 경우
            if not mt[i]:
                temp = i
                break
            # 인덱스가 가장 큰 경우 
            elif mt[i][0] > idx:
                idx = mt[i][0]
                temp = i

        # 해당 콘센트 제거 후 추가
        plug.remove(temp)
        plug.append(p)
        if mt[p]:
            mt[p].pop(0)
        
        cnt+=1

print(cnt)