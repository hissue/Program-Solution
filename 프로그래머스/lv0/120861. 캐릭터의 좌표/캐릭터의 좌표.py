def solution(keyinput, board):
    x = 0
    y = 0
    
    # 위, 아래, 왼쪽, 오른쪽
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    garo = board[0]//2
    sero = board[1]//2  
                 
    for direction in keyinput:
        if direction == "up":
            i=0
        elif direction == "down":
            i=1
        elif direction == "left":
            i=2
        else:
            i=3
            
        if -garo <= x+dx[i] <= garo and -sero <= y+dy[i] <= sero:
            x+=dx[i]
            y+=dy[i]
    return [x,y]