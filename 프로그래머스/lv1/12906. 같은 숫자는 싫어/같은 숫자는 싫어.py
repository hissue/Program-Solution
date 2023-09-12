def solution(arr):
    stack = []
    for _ in arr:
        if not stack or stack[-1] != _:
            stack.append(_)
    return stack