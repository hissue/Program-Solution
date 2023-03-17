import sys
sys.setrecursionlimit(10**6)

nums = []

while True:
    try:
        num = int(input())
        nums.append(num)
    except:
        break


def inorder(start,end):
    if start > end:
        return 
    
    mid = end+1
    for i in range(start+1,end+1):
        if nums[start] < nums[i]:
            mid = i
            break

    inorder(start+1,mid-1)
    inorder(mid,end)
    print(nums[start])

inorder(0,len(nums)-1)