def solution(myString, pat):
    stack = list(myString)
    count=0
    idx=1
    
    for myStr in myString[::-1]:
        if myStr != pat[-idx]:
            stack.pop()
            count=0
        else:
            idx+=1
            count+=1
        
        if count == len(pat):
            return "".join(stack)
        