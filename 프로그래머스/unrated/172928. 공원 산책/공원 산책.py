def solution(park, routes):
    # E, W, N, S
    direction = {"E" : 1,"W" :-1,"N" :-1,"S" :1}
    
    # 시작 지점
    for a in range(len(park)):
        if "S" in park[a]:
            x = park[a].index("S")
            y = a
            break
            
    # 명령 수행     
    row,col = len(park),len(park[0])
    for route in routes:
        d, w = route.split(" ")
        temp = direction[d] * int(w)
        flag = 1
        if d == "E" or d == "W":
            if 0 <= x + temp < col:
                if d == "E" and "X" in park[y][x+1:x+temp+1] :
                    flag = 0
                elif d == "W" and "X" in park[y][x+temp:x]:
                    flag = 0
                if flag:
                    x += temp    
        else:
            if 0 <= y + temp < row:
                if d == "S":
                    for idx in range(y+1, y+temp+1):
                        if park[idx][x] == "X":
                            flag = 0
                            break
                elif d == "N":
                    for idx in range(y-1, y+temp-1,-1):
                        if park[idx][x] == "X":
                            flag = 0
                            break
                if flag:
                    y += temp    
                
    return [y,x]