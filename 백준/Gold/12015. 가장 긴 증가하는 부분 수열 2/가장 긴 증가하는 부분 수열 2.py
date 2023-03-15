import sys

N = int(sys.stdin.readline())
cases = [*map(int,sys.stdin.readline().split())]
LIS = [0]

for case in cases:
    if LIS[-1] < case:
        LIS.append(case)

    else:
        left = 0
        right = len(LIS)

        while left<right:
            mid = (left+right)//2

            if LIS[mid] < case:
                left = mid+1

            else:
                right = mid
        
        LIS[right] = case

print(len(LIS)-1)