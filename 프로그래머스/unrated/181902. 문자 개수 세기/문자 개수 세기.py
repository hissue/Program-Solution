def solution(my_string):
    answer = [0 for _ in range(26*2)]
    for my in my_string:
        if my.isupper():
            answer[ord(my)%ord("A")] +=1    
        else:
            answer[ord(my)%ord("a")+26] +=1
    return answer