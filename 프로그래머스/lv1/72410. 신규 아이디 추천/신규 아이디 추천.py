def solution(new_id):
    answer = ''
    #1
    new_id = new_id.lower()
    #2
    for data in new_id:
        if data.islower() or data.isdigit() or data == "-" or data == "_" or data == ".":
            answer+=data
    #3
    # answer = answer.replace("."," ")
    for i in range(answer.count("."),0,-1):
        answer = answer.replace("."*i," ")  
    #4
    answer = answer.strip()
    #5
    if not answer:
        answer+="a"
    #6
    if len(answer) >=16:
        answer = answer[:15].strip()
    #7
    if len(answer) <= 2:
        answer +=answer[-1]*(3-len(answer))
        
    answer = answer.replace(" ",".")  
        
    return answer