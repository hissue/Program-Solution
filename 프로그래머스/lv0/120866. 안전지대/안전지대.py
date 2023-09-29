def solution(board):
    answer = []
    length = len(board)
    dr = [-1,-1,-1,0,0,1,1,1]
    dc = [-1,0,1,-1,1,-1,0,1]
    for r in range(length):
        for c in range(length):
            if board[r][c]:
                answer.append([r,c])
                for i in range(8):
                    if 0 <= r+dr[i] < length and 0<=c+dc[i]<length:
                        answer.append([r+dr[i],c+dc[i]])
    return length**2 - len(list(set(map(tuple,answer))))