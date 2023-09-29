def solution(lottos, win_nums):
    answer = [6,6,5,4,3,2,1]
    zero = lottos.count(0)
    count = 0
    for data in win_nums:
        if data in lottos:
            count+=1
            
    return [answer[zero+count],answer[count]]