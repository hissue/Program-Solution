import sys
wood = list(map(int,sys.stdin.readline().split()))
i = 1
while wood != [1,2,3,4,5]:
    
    if wood[i-1] > wood[i]:
        wood[i-1],wood[i] = wood[i],wood[i-1]
        print(*wood)

    i=i%4+1