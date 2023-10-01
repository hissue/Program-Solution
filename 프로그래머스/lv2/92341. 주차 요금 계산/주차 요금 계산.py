import math
def solution(fees, records):
    dirci = {}
    answer = 0
    baseTime = fees[0]
    baseRate = fees[1]
    perTime = fees[2]
    perRate = fees[3]
    carRate=[]
    for record in records:
        t,n,e = record.split(" ")
        if e == "IN":
            if n in dirci:
                dirci[n].append([t,e])
            else:
                dirci[n]= [[t,e]]
        else:
            dirci[n].append([t,e])

    for k in sorted(list(dirci.keys())):
        stack = []
        totalTime = 0
        for data in sorted(dirci[k]):
            stack.append(data)
            if len(stack) == 2:
                inTime = stack[0][0].split(":")
                outTime = stack[1][0].split(":")
                totalTime += (int(outTime[0]) - int(inTime[0]))*60+(int(outTime[1]) - int(inTime[1]))
                stack = []
        if stack:
            inTime = stack[0][0].split(":")
            outTime = [23,59]    
            totalTime += (int(outTime[0]) - int(inTime[0]))*60+(int(outTime[1]) - int(inTime[1]))
        
        if totalTime <= baseTime:
            carRate.append(baseRate)
        else:
            carRate.append(baseRate+math.ceil((totalTime-baseTime)/perTime)*perRate)     
        
    return carRate