import collections
def solution(A, B):
    answer = B[::-1]
    stack = collections.deque(A[::-1])
    count=0
    for _ in range(len(A)):
        if answer == "".join(stack):
            break
        stack.append(stack.popleft())
        count+=1

    return -1 if count == len(A) else count