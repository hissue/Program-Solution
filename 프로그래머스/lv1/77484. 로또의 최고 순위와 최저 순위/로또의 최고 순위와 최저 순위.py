import collections
def solution(lottos, win_nums):
    zero = lottos.count(0)
    count = 0
    result = []
    for data in win_nums:
        if data in lottos:
            lottos.remove(data)
            count+=1
            
    for data in [zero+count,count]:
        if data == 6:
            result.append(1)        
        elif data == 5:
            result.append(2)        
        elif data == 4:
            result.append(3)        
        elif data == 3:
            result.append(4)        
        elif data == 2:
            result.append(5)        
        else:
            result.append(6)
    
    return result