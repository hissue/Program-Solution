from collections import deque
def check(s):
    stack = []
    for data in s:
        if stack:
            if stack[-1] == "[" and data == "]":
                stack.pop()
            elif stack[-1] == "(" and data == ")":
                stack.pop()
            elif stack[-1] == "{" and data == "}":
                stack.pop()
            else:
                stack.append(data)
        else:
            stack.append(data)
    return stack

def solution(s):
    answer = 0
    queue = deque(s)
    for _ in range(len(s)):
        if not check(queue):
            answer += 1
        queue.append(queue.popleft())
        
    return answer