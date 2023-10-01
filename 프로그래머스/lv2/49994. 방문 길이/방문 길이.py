def solution(dirs):
    answer = []
    x,y = 0,0
    count = 0
    direction = {"U": [0,1], "D": [0,-1], "R": [1,0], "L": [-1,0]}
    for d in dirs:
        dx,dy = direction[d]
        if -5<=x+dx<=5 and -5<=y+dy<=5:
            if [[x,y],[x+dx,y+dy]] not in answer and [[x+dx,y+dy],[x,y]]:
                answer.append([[x,y],[x+dx,y+dy]])
                answer.append([[x+dx,y+dy],[x,y]])
                count+=1
            x+=dx
            y+=dy
    
    return count