def solution(dots):
    x,y = dots[0]
    for idx in range(1,len(dots)):
        if x == dots[idx][0]:
            height = abs(y-dots[idx][1])
        elif y == dots[idx][1]:
            width = abs(x-dots[idx][0])
        
            
    return height*width