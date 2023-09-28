def solution(N, stages):
    stagesDict = [0 for _ in range(N+1)]
    answer = []
    result = []
    for stage in stages:
        stagesDict[stage-1] +=1
    
    for idx in range(len(stagesDict)-1):
        if stagesDict[idx]:
            answer.append([idx,stagesDict[idx]/sum(stagesDict[idx:])])
        else:
            answer.append([idx,0])
    
    answer.sort(key=lambda x : -x[1])

    for i in range(N):
        result.append(answer[i][0]+1)
    
    return result