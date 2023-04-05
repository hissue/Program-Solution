import sys

# 자기 앞에 자기보다 큰 학생이 없다면 append
# 자기 앞에 자기보다 큰 학생이 있다면 그 앞에 삽입하고 cnt+=1

P = int(input())

for _ in range(P):
    arr = list(map(int,sys.stdin.readline().split()))
    cnt=0
    for i in range(1,len(arr)):
        for j in range(1,i):
            if arr[i] < arr[j]:
                cnt+=1
    print(arr[0],cnt)