def solution(nums):
    answer = {}
    count = 0
    for data in nums:
        if data in answer:
            answer[data] +=1
        else:
            answer[data] = 1
    for k in answer.keys():
        if count == len(nums)//2:
            break
        count+=1
    return count