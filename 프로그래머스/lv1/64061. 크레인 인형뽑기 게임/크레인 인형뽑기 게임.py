def solution(board, moves):
    answer = 0
    stack = []
    length = len(board)
    for idx in moves:
        for match in range(length):
            if board[match][idx-1]:
                stack.append(board[match][idx-1])
                board[match][idx-1] = 0
                break
        if len(stack) > 1 and stack[-2] == stack[-1]:
            stack = stack[:-2]
            answer+=2
    return answer