def solution(cards1, cards2, goal):
    length = len(goal)
    for word in range(length):
        if cards1 and goal[0] == cards1[0]:
            goal.pop(0)
            cards1.pop(0)
        elif cards2 and goal[0] == cards2[0]:
            goal.pop(0)
            cards2.pop(0)
    return "Yes" if not goal else "No"