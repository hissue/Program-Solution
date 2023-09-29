def solution(players, callings):
    current = {data:idx for idx,data in enumerate(players)}
    index = {idx:data for idx,data in enumerate(players)}
    answer = ["" for _ in range(len(players))]
    for calling in callings:
        old_name = index[current[calling]-1] 
        current[calling] -=1
        current[old_name] +=1
        index[current[calling]]= calling
        index[current[calling]+1] = old_name
        
    for k,v in current.items():
        answer[v] = k
    return answer