from collections import deque
def solution(s):
    answer = True
    stack = [s[0]]
    for i in range(1,len(s)):
        if '(' == s[i]:
            stack.append(s[i])
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            
    if stack:
        return False
    
    else:
        return True