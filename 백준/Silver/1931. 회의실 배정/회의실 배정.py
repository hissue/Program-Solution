# 한 개의 회의실이 있을 경우 N개의 회의에 대하여 회의실 사용표 제작
# 시작 시간과 끝 시간이 겹치지 않게 하면서 회의실을 사용할 수 있는 최대 개수는?
# 한 회의 끝남과 동시에 다음 회의 시작 가능하며, 회의 시작과 끝나는 시간이 같을 수 있음
import sys
N = int(sys.stdin.readline())

meeting = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

meeting.sort(key=lambda x : (x[1],x[0]))

temp = 0
cnt = 0

for s,e in meeting:
    if s >= temp:
        temp = e
        cnt+=1
print(cnt)