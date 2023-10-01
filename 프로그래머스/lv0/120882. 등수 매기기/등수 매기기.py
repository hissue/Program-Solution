def solution(score):
    answer = []
    result = [0 for _ in range(len(score))]
    for i,v in enumerate(score):
        answer.append([sum(v)/2,i])
    answer.sort(reverse=True)
    answer[0].append(1)
    count = 1
    for idx in range(1,len(answer)):
        if answer[idx-1][0] == answer[idx][0]:
            count+=1
            answer[idx].append(answer[idx-1][2])
        else:
            answer[idx].append(answer[idx-1][2]+count)
            count=1
            
    for data in answer:
        result[data[1]]=(data[2])
        
    return result