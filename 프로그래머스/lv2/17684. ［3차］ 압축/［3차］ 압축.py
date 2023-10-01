def solution(msg):
    answer = {chr(idx) : idx%ord("A")+1 for idx in range(ord("A"),ord("Z")+1)}
    result = []
    length = len(msg)
    i = 0
    index = 27
    while i < length:
        word = msg[i]
        
        idx=1
        while i+idx < length and word in answer.keys():
            word+=msg[i+idx]
            idx+=1
        i+=idx-1
        if word in answer.keys():
            result.append(answer[word])
            i+=1
        else:
            result.append(answer[word[:-1]])
            answer[word] = index

        index+=1
        
    return result