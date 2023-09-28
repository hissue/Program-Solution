def solution(participant, completion):
    participants = {}
    for person in participant:
        if person in participants:
            participants[person] +=1
        else:
            participants[person] =1
    
    for comPerson in completion:
        participants[comPerson]-=1

    for person in participant:
        if participants[person]:
            return person