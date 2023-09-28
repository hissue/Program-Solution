def solution(my_string):
    temp = my_string.split(" ")
    answer = int(temp[0])
    for idx in range(2,len(temp),2):
        if temp[idx-1] == "+":
            answer+=int(temp[idx])
        elif temp[idx-1] == "-":
            answer-=int(temp[idx])
            
    return answer