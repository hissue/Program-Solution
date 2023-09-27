def solution(answers):
    number1 = "12345"*2000
    number2 = "21232425"*1250
    number3 = "3311224455"*1000
    count = [0,0,0]
    answer = []
    for i in range(len(answers)):
        if str(answers[i]) == number1[i]:
            count[0]+=1
        if str(answers[i]) == number2[i]:
            count[1]+=1
        if str(answers[i]) == number3[i]:
            count[2]+=1
    
    maxValue = max(count)
    for idx in range(3):
        if maxValue == count[idx]:
            answer.append(idx+1)
    
    return sorted(answer)