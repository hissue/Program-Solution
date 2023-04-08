import sys
from collections import deque

def dfs(numbers, target, depth, value):
    answer = 0
    if depth == len(numbers):
        if value == target:
            return 1
        else:
            return 0
    answer += dfs(numbers, target, depth+1, value + numbers[depth])
    answer += dfs(numbers, target, depth+1, value - numbers[depth])
    return answer

def solution(numbers, target):
    answer = dfs(numbers, target, 0, 0)
    return answer