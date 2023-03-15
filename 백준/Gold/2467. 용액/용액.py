import sys

N = int(sys.stdin.readline())
liquid = [*map(int,sys.stdin.readline().split())]

start = result_left = 0
end = result_right = len(liquid)-1
total = sys.maxsize

while start<end:
    mid = (start+end)//2
    temp = liquid[start] + liquid[end]
    if  abs(temp) < total:
        total = abs(temp)
        result_left = start
        result_right = end

    if temp < 0:
        start+=1
    else:
        end -=1

print(liquid[result_left],liquid[result_right])