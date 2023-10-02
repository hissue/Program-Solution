ids = {}
answer = []
def changeName(user,sentence):
    if ids[user[1]][0] != user[2]:
        oldName, index = ids[user[1]]
        ids[user[1]][0] = user[2]
        for i in index:
            answer[i]=answer[i].replace(oldName, user[2])       
            
    return user[2]+sentence if sentence else "" 
        
def solution(record):
    index = 0
    for r in record:
        user = r.split(" ")
        if user[0] == "Enter":
            if user[1] not in ids:
                ids[user[1]] = [user[2],[]]
            answer.append(changeName(user,"님이 들어왔습니다."))
            ids[user[1]][1].append(index)
            index+=1
        elif user[0] == "Leave":
            answer.append(ids[user[1]][0]+"님이 나갔습니다.")
            ids[user[1]][1].append(index)
            index+=1
        else:
            changeName(user,"")
        
    return answer