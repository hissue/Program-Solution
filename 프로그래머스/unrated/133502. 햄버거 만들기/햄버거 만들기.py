def solution(ingredient):
    answer = 0
    stack = []
    for data in ingredient:
        stack.append(data)
        if len(stack) > 3 and stack[-4:] == [1,2,3,1]:
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            answer+=1
            
            
    return answer